#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseRedirect
from django.views.generic import View
from .models import Comment, CommentUser
import json
from django.views.decorators.csrf import csrf_exempt
from login_szu import login_szu
# Create your views here.


def get_comment(request):
    pk = request.GET.get('pk')
    if not pk:
        return HttpResponseNotFound()
    comments = Comment.objects.filter(article=pk)
    deal_dict = {}
    deal_dict['commentCount'] = len(comments)
    comments_array = [{
                            'userName': i.user.name[0]+u'同学',
                            'commentContent': i.content,
                            'gender': i.user.gender,
                            'createTime': i.create_time.strftime("%y-%m-%d"),
                            'collega': i.user.collega
                        } for i in comments]
    deal_dict['comment'] = comments_array
    return HttpResponse(json.dumps(deal_dict, ensure_ascii=False), content_type="application/json")

@csrf_exempt
def add_comment(request):
    if request.method == "GET":
        return HttpResponseBadRequest("GET")
    '''
        {
            commentContent: (string),
            articleId: (int)
            }
        关键是对当前有没用户的判断
    '''
    #一般是已经登陆的，但需要考虑到历史的进程，也需要靠自身的努力，所以判断一下有没有没登陆的吧
    try:
        if not request.session['szu_no']:
            return HttpResponseBadRequest("没登陆别评论")
    except:
        return HttpResponseBadRequest("没登陆别评论")
    
    #判断是否保存用户信息
    users = CommentUser.objects.filter(stu_no=request.session["szu_no"])
    
    if not users:
        #没有注册的情况，继续注册
        try:
            CommentUser.objects.create(stu_no=request.session['szu_no'], gender=request.session['szu_sex'], name=request.session['szu_name'], collega=request.session['szu_org_name'])
        except:
            return HttpResponseBadRequest(request.session.items())
        users = CommentUser.objects.filter(stu_no=request.session['szu_no'])
    
    user = users[0]
    data = request.POST
    #接下来就是一些验证了
    newComment = Comment.objects.create(user=user, content=data['commentContent'], article=data['articleId'])
    #然后就欧克了
    success_dict = {
        'userName': newComment.user.name[0] + u'同学',
        'commentContent': newComment.content,
        'gender': newComment.user.gender,
        'createTime': newComment.create_time.strftime('%y-%m-%d'),
        'collega': newComment.user.collega
    }
    return HttpResponse(json.dumps(success_dict, ensure_ascii=False), content_type="application/json")

def szu_oauth_info(request):
    try:
        if request.session['szu_no']:
            info_dict = {
                'isLogin': True,
                'userStuNo': request.session['szu_no']
            }
            return HttpResponse(json.dumps(info_dict), content_type="application/json")
    except:
        pass
    info_dict = {
        'isLogin': False,
        'userStuNo': ''
    }
    return HttpResponse(json.dumps(info_dict), content_type="application/json")

@login_szu
def szu_login(request):
    redict_url = request.GET.get('redi')
    if redict_url:
        return HttpResponseRedirect(redict_url)
    return HttpResponseBadRequest('error')
