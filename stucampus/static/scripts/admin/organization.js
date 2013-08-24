(function($,$S){
    if (typeof $S.Organization == 'undefined'){
        $S.Organization = {};
    }

    /**
    * 定义快速创建组织函数
    */
    $S.Organization.create = function(){
        var name = $("#name").val();
        var phone = $("#phone").val();
        url = '/manage/organization/list';
        method = 'POST';
        data = {'name': name, 'phone': phone};
        $S.ajax(url, method, data);
    };

    $S.Organization.add_manager = function(id){
        var email = $("#org-"+id).val();
        url = '/manage/organization/' + id + '/manager';
        method = 'POST';
        data = {'email': email};
        $S.ajax(url, method, data);
    };

    $S.Organization.remove = function(id){
        url = '/manage/organization/' + id;
        method = 'DELETE';
        $S.ajax(url, method);
    };

})(jQuery, StuCampus);
