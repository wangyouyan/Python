# coding:utf-8

from django.db.models import Q
from jasset.asset_api import *
from jumpserver.api import *
from jumpserver.models import Setting
from jasset.forms import AssetForm, IdcForm,TenantForm,IdracForm,UrlForm,VirtualForm,VirtualHostForm
from jasset.models import Asset, IDC, AssetGroup, ASSET_TYPE, ASSET_STATUS,Tenant_info,Idrac,Url_info,Virtual_platform,Virtual_host
from jperm.perm_api import get_group_asset_perm, get_group_user_perm


@require_role('admin')
def group_add(request):
    """
    Group add view
    添加资产组
    """
    header_title, path1, path2 = u'添加资产组', u'资产管理', u'添加资产组'
    asset_all = Asset.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        asset_select = request.POST.getlist('asset_select', [])
        comment = request.POST.get('comment', '')

        try:
            if not name:
                emg = u'组名不能为空'
                raise ServerError(emg)

            asset_group_test = get_object(AssetGroup, name=name)
            if asset_group_test:
                emg = u"该组名 %s 已存在" % name
                raise ServerError(emg)

        except ServerError:
            pass

        else:
            db_add_group(name=name, comment=comment, asset_select=asset_select)
            smg = u"主机组 %s 添加成功" % name

    return my_render('jasset/group_add.html', locals(), request)


@require_role('admin')
def group_edit(request):
    """
    Group edit view
    编辑资产组
    """
    header_title, path1, path2 = u'编辑主机组', u'资产管理', u'编辑主机组'
    group_id = request.GET.get('id', '')
    group = get_object(AssetGroup, id=group_id)

    asset_all = Asset.objects.all()
    asset_select = Asset.objects.filter(group=group)
    asset_no_select = [a for a in asset_all if a not in asset_select]

    if request.method == 'POST':
        name = request.POST.get('name', '')
        asset_select = request.POST.getlist('asset_select', [])
        comment = request.POST.get('comment', '')

        try:
            if not name:
                emg = u'组名不能为空'
                raise ServerError(emg)

            if group.name != name:
                asset_group_test = get_object(AssetGroup, name=name)
                if asset_group_test:
                    emg = u"该组名 %s 已存在" % name
                    raise ServerError(emg)

        except ServerError:
            pass

        else:
            group.asset_set.clear()
            db_update_group(id=group_id, name=name, comment=comment, asset_select=asset_select)
            smg = u"主机组 %s 添加成功" % name

        return HttpResponseRedirect(reverse('asset_group_list'))

    return my_render('jasset/group_edit.html', locals(), request)


@require_role('admin')
def group_list(request):
    """
    list asset group
    列出资产组
    """
    header_title, path1, path2 = u'查看资产组', u'资产管理', u'查看资产组'
    keyword = request.GET.get('keyword', '')
    asset_group_list = AssetGroup.objects.all()
    group_id = request.GET.get('id')
    if group_id:
        asset_group_list = asset_group_list.filter(id=group_id)
    if keyword:
        asset_group_list = asset_group_list.filter(Q(name__contains=keyword) | Q(comment__contains=keyword))

    asset_group_list, p, asset_groups, page_range, current_page, show_first, show_end = pages(asset_group_list, request)
    return my_render('jasset/group_list.html', locals(), request)


@require_role('admin')
def group_del(request):
    """
    Group delete view
    删除主机组
    """
    group_ids = request.GET.get('id', '')
    group_id_list = group_ids.split(',')

    for group_id in group_id_list:
        AssetGroup.objects.filter(id=group_id).delete()

    return HttpResponse(u'删除成功')


@require_role('admin')
def asset_add(request):
    """
    Asset add view
    添加资产
    """
    header_title, path1, path2 = u'添加资产', u'资产管理', u'添加资产'
    asset_group_all = AssetGroup.objects.all()
    af = AssetForm()
    default_setting = get_object(Setting, name='default')
    default_port = default_setting.field2 if default_setting else ''
    if request.method == 'POST':
        af_post = AssetForm(request.POST)
        ip = request.POST.get('ip', '')
        hostname = request.POST.get('hostname', '')
        is_active = True if request.POST.get('is_active') == '1' else False
        use_default_auth = request.POST.get('use_default_auth', '')
        try:
            if Asset.objects.filter(hostname=unicode(hostname)):
                error = u'该主机名 %s 已存在!' % hostname
                raise ServerError(error)
            if len(hostname) > 54:
                error = u"主机名长度不能超过53位!"
                raise ServerError(error)
        except ServerError:
            pass
        else:
            if af_post.is_valid():
                asset_save = af_post.save(commit=False)
                if not use_default_auth:
                    password = request.POST.get('password', '')
                    password_encode = CRYPTOR.encrypt(password)
                    asset_save.password = password_encode
                if not ip:
                    asset_save.ip = hostname
                asset_save.is_active = True if is_active else False
                asset_save.save()
                af_post.save_m2m()

                msg = u'主机 %s 添加成功' % hostname
            else:
                esg = u'主机 %s 添加失败' % hostname

    return my_render('jasset/asset_add.html', locals(), request)


@require_role('admin')
def asset_add_batch(request):
    header_title, path1, path2 = u'添加资产', u'资产管理', u'批量添加'
    return my_render('jasset/asset_add_batch.html', locals(), request)


@require_role('admin')
def asset_del(request):
    """
    del a asset
    删除主机
    """
    asset_id = request.GET.get('id', '')
    if asset_id:
        Asset.objects.filter(id=asset_id).delete()

    if request.method == 'POST':
        asset_batch = request.GET.get('arg', '')
        asset_id_all = str(request.POST.get('asset_id_all', ''))

        if asset_batch:
            for asset_id in asset_id_all.split(','):
                asset = get_object(Asset, id=asset_id)
                asset.delete()

    return HttpResponse(u'删除成功')


@require_role(role='super')
def asset_edit(request):
    """
    edit a asset
    修改主机
    """
    header_title, path1, path2 = u'修改资产', u'资产管理', u'修改资产'

    asset_id = request.GET.get('id', '')
    username = request.user.username
    asset = get_object(Asset, id=asset_id)
    if asset:
        password_old = asset.password
    # asset_old = copy_model_instance(asset)
    af = AssetForm(instance=asset)
    if asset.remote_ip:
        remote_instance = get_object(Idrac,Idrac_ip=asset.remote_ip.Idrac_ip)
    else:
        remote_instance = None
    Idrac_form = IdracForm(instance=remote_instance)
    if request.method == 'POST':
        af_post = AssetForm(request.POST, instance=asset)
        remote_ip_post = IdracForm(request.POST, instance=remote_instance)
        ip = request.POST.get('ip', '')
        hostname = request.POST.get('hostname', '')
        password = request.POST.get('password', '')
        is_active = True if request.POST.get('is_active') == '1' else False
        use_default_auth = request.POST.get('use_default_auth', '')
        try:
            asset_test = get_object(Asset, hostname=hostname)
            if asset_test and asset_id != unicode(asset_test.id):
                emg = u'该主机名 %s 已存在!' % hostname
                raise ServerError(emg)
            if len(hostname) > 54:
                emg = u'主机名长度不能超过54位!'
                raise ServerError(emg)
            else:
                if af_post.is_valid():
                    af_save = af_post.save(commit=False)
                    if use_default_auth:
                        af_save.username = ''
                        af_save.password = ''
                        # af_save.port = None
                    else:
                        if password:
                            password_encode = CRYPTOR.encrypt(password)
                            af_save.password = password_encode
                        else:
                            af_save.password = password_old
                    af_save.is_active = True if is_active else False
                    # print remote_ip_post
                    if remote_ip_post.is_valid():
                        rf_save = remote_ip_post.save()
                        af_save.remote_ip=rf_save
                    af_save.save()
                    af_post.save_m2m()
                    # asset_new = get_object(Asset, id=asset_id)
                    # asset_diff_one(asset_old, asset_new)
                    info = asset_diff(af_post.__dict__.get('initial'), request.POST)
                    # print af_post.__dict__.get('initial') # 获取表单初始的数据
                    # print remote_ip_post.__dict__.get('initial')
                    remote_info = asset_diff(remote_ip_post.__dict__.get('initial'), request.POST)
                    # print remote_info
                    db_asset_alert(asset, username, info)
                    db_asset_alert(asset, username, remote_info)

                    smg = u'主机 %s 修改成功' % ip
                else:
                    emg = u'主机 %s 修改失败' % ip
                    raise ServerError(emg)
        except ServerError as e:
            error = e.message
            return my_render('jasset/asset_edit.html', locals(), request)
        return HttpResponseRedirect(reverse('asset_detail')+'?id=%s' % asset_id)

    return my_render('jasset/asset_edit.html', locals(), request)


@require_role('user')
def asset_list(request):
    """
    asset list view
    """
    header_title, path1, path2 = u'查看资产', u'资产管理', u'查看资产'
    username = request.user.username
    user_perm = request.session['role_id']
    idc_all = IDC.objects.filter()
    asset_group_all = AssetGroup.objects.all()
    asset_types = ASSET_TYPE
    asset_status = ASSET_STATUS
    envs = ASSET_ENV
    idc_name = request.GET.get('idc', '')
    group_name = request.GET.get('group', '')
    asset_type = request.GET.get('asset_type', '')
    env = request.GET.get('env', '')
    status = request.GET.get('status', '')
    keyword = request.GET.get('keyword', '')
    export = request.GET.get("export", False)
    group_id = request.GET.get("group_id", '')
    idc_id = request.GET.get("idc_id", '')
    asset_id_all = request.GET.getlist("id", '')

    if group_id:
        group = get_object(AssetGroup, id=group_id)
        if group:
            asset_find = Asset.objects.filter(group=group)
    elif idc_id:
        idc = get_object(IDC, id=idc_id)
        if idc:
            asset_find = Asset.objects.filter(idc=idc)
    else:
        if user_perm != 0:
            asset_find = Asset.objects.all()
        else:
            asset_id_all = []
            user = get_object(User, username=username)
            asset_perm = get_group_user_perm(user) if user else {'asset': ''}
            user_asset_perm = asset_perm['asset'].keys()
            for asset in user_asset_perm:
                asset_id_all.append(asset.id)
            asset_find = Asset.objects.filter(pk__in=asset_id_all)
            asset_group_all = list(asset_perm['asset_group'])

    if idc_name:
        asset_find = asset_find.filter(idc__name__contains=idc_name)

    if group_name:
        asset_find = asset_find.filter(group__name__contains=group_name)

    if asset_type:
        asset_find = asset_find.filter(asset_type__contains=asset_type)

    if status:
        asset_find = asset_find.filter(status__contains=status)
    if env:
        print env
        asset_find = asset_find.filter(env__contains=env)

    if keyword:
        asset_find = asset_find.filter(
            Q(hostname__contains=keyword) |
            Q(other_ip__contains=keyword) |
            Q(ip__contains=keyword) |
            Q(remote_ip__contains=keyword) |
            Q(comment__contains=keyword) |
            Q(username__contains=keyword) |
            Q(group__name__contains=keyword) |
            Q(cpu__contains=keyword) |
            Q(memory__contains=keyword) |
            Q(disk__contains=keyword) |
            Q(brand__contains=keyword) |
            Q(cabinet__contains=keyword) |
            Q(sn__contains=keyword) |
            Q(system_type__contains=keyword) |
            Q(system_version__contains=keyword))

    if export:
        if asset_id_all:
            asset_find = []
            for asset_id in asset_id_all:
                asset = get_object(Asset, id=asset_id)
                if asset:
                    asset_find.append(asset)
        s = write_excel(asset_find)
        if s[0]:
            file_name = s[1]
        smg = u'excel文件已生成，请点击下载!'
        return my_render('jasset/asset_excel_download.html', locals(), request)
    assets_list, p, assets, page_range, current_page, show_first, show_end = pages(asset_find, request)
    if user_perm != 0:
        return my_render('jasset/asset_list.html', locals(), request)
    else:
        return my_render('jasset/asset_cu_list.html', locals(), request)


@require_role('admin')
def asset_edit_batch(request):
    af = AssetForm()
    name = request.user.username
    asset_group_all = AssetGroup.objects.all()

    if request.method == 'POST':
        env = request.POST.get('env', '')
        idc_id = request.POST.get('idc', '')
        port = request.POST.get('port', '')
        use_default_auth = request.POST.get('use_default_auth', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        group = request.POST.getlist('group', [])
        cabinet = request.POST.get('cabinet', '')
        comment = request.POST.get('comment', '')
        asset_id_all = unicode(request.GET.get('asset_id_all', ''))
        asset_id_all = asset_id_all.split(',')
        for asset_id in asset_id_all:
            alert_list = []
            asset = get_object(Asset, id=asset_id)
            if asset:
                if env:
                    if asset.env != env:
                        asset.env = env
                        alert_list.append([u'运行环境', asset.env, env])
                if idc_id:
                    idc = get_object(IDC, id=idc_id)
                    name_old = asset.idc.name if asset.idc else u''
                    if idc and idc.name != name_old:
                        asset.idc = idc
                        alert_list.append([u'机房', name_old, idc.name])
                if port:
                    if unicode(asset.port) != port:
                        asset.port = port
                        alert_list.append([u'端口号', asset.port, port])

                if use_default_auth:
                    if use_default_auth == 'default':
                        asset.use_default_auth = 1
                        asset.username = ''
                        asset.password = ''
                        alert_list.append([u'使用默认管理账号', asset.use_default_auth, u'默认'])
                    elif use_default_auth == 'user_passwd':
                        asset.use_default_auth = 0
                        asset.username = username
                        password_encode = CRYPTOR.encrypt(password)
                        asset.password = password_encode
                        alert_list.append([u'使用默认管理账号', asset.use_default_auth, username])
                if group:
                    group_new, group_old, group_new_name, group_old_name = [], asset.group.all(), [], []
                    for group_id in group:
                        g = get_object(AssetGroup, id=group_id)
                        if g:
                            group_new.append(g)
                    if not set(group_new) < set(group_old):
                        group_instance = list(set(group_new) | set(group_old))
                        for g in group_instance:
                            group_new_name.append(g.name)
                        for g in group_old:
                            group_old_name.append(g.name)
                        asset.group = group_instance
                        alert_list.append([u'主机组', ','.join(group_old_name), ','.join(group_new_name)])
                if cabinet:
                    if asset.cabinet != cabinet:
                        asset.cabinet = cabinet
                        alert_list.append([u'机柜号', asset.cabinet, cabinet])
                if comment:
                    if asset.comment != comment:
                        asset.comment = comment
                        alert_list.append([u'备注', asset.comment, comment])
                asset.save()

            if alert_list:
                recode_name = unicode(name) + ' - ' + u'批量'
                AssetRecord.objects.create(asset=asset, username=recode_name, content=alert_list)
        return my_render('jasset/asset_update_status.html', locals(), request)

    return my_render('jasset/asset_edit_batch.html', locals(), request)


@require_role('admin')
def asset_detail(request):
    """
    Asset detail view
    """
    header_title, path1, path2 = u'主机详细信息', u'资产管理', u'主机详情'
    asset_id = request.GET.get('id', '')
    asset = get_object(Asset, id=asset_id)
    perm_info = get_group_asset_perm(asset)
    log = Log.objects.filter(host=asset.hostname)
    if perm_info:
        user_perm = []
        for perm, value in perm_info.items():
            if perm == 'user':
                for user, role_dic in value.items():
                    user_perm.append([user, role_dic.get('role', '')])
            elif perm == 'user_group' or perm == 'rule':
                user_group_perm = value
    print perm_info

    asset_record = AssetRecord.objects.filter(asset=asset).order_by('-alert_time')

    return my_render('jasset/asset_detail.html', locals(), request)


@require_role('admin')
def asset_update(request):
    """
    Asset update host info via ansible view
    """
    asset_id = request.GET.get('id', '')
    asset = get_object(Asset, id=asset_id)
    name = request.user.username
    if not asset:
        return HttpResponseRedirect(reverse('asset_detail')+'?id=%s' % asset_id)
    else:
        asset_ansible_update([asset], name)
    return HttpResponseRedirect(reverse('asset_detail')+'?id=%s' % asset_id)


@require_role('admin')
def asset_update_batch(request):
    if request.method == 'POST':
        arg = request.GET.get('arg', '')
        name = unicode(request.user.username) + ' - ' + u'自动更新'
        if arg == 'all':
            asset_list = Asset.objects.all()
        else:
            asset_list = []
            asset_id_all = unicode(request.POST.get('asset_id_all', ''))
            asset_id_all = asset_id_all.split(',')
            for asset_id in asset_id_all:
                asset = get_object(Asset, id=asset_id)
                if asset:
                    asset_list.append(asset)
        asset_ansible_update(asset_list, name)
        return HttpResponse(u'批量更新成功!')
    return HttpResponse(u'批量更新成功!')


@require_role('admin')
def idc_add(request):
    """
    IDC add view
    """
    header_title, path1, path2 = u'添加IDC', u'资产管理', u'添加IDC'
    if request.method == 'POST':
        idc_form = IdcForm(request.POST)
        if idc_form.is_valid():
            idc_name = idc_form.cleaned_data['name']

            if IDC.objects.filter(name=idc_name):
                emg = u'添加失败, 此IDC %s 已存在!' % idc_name
                return my_render('jasset/idc_add.html', locals(), request)
            else:
                idc_form.save()
                smg = u'IDC: %s添加成功' % idc_name
            return HttpResponseRedirect(reverse('idc_list'))
    else:
        idc_form = IdcForm()
    return my_render('jasset/idc_add.html', locals(), request)


@require_role('admin')
def idc_list(request):
    """
    IDC list view
    """
    header_title, path1, path2 = u'查看IDC', u'资产管理', u'查看IDC'
    posts = IDC.objects.all()
    keyword = request.GET.get('keyword', '')
    if keyword:
        posts = IDC.objects.filter(Q(name__contains=keyword) | Q(comment__contains=keyword))
    else:
        posts = IDC.objects.exclude(name='ALL').order_by('id')
    contact_list, p, contacts, page_range, current_page, show_first, show_end = pages(posts, request)
    return my_render('jasset/idc_list.html', locals(), request)


@require_role('admin')
def idc_edit(request):
    """
    IDC edit view
    """
    header_title, path1, path2 = u'编辑IDC', u'资产管理', u'编辑IDC'
    idc_id = request.GET.get('id', '')
    idc = get_object(IDC, id=idc_id)
    if request.method == 'POST':
        idc_form = IdcForm(request.POST, instance=idc)
        if idc_form.is_valid():
            idc_form.save()
            return HttpResponseRedirect(reverse('idc_list'))
    else:
        idc_form = IdcForm(instance=idc)
        return my_render('jasset/idc_edit.html', locals(), request)


@require_role('admin')
def idc_del(request):
    """
    IDC delete view
    """
    idc_ids = request.GET.get('id', '')
    idc_id_list = idc_ids.split(',')

    for idc_id in idc_id_list:
        IDC.objects.filter(id=idc_id).delete()

    return HttpResponseRedirect(reverse('idc_list'))


@require_role('admin')
def asset_upload(request):
    """
    Upload asset excel file view
    """
    if request.method == 'POST':
        excel_file = request.FILES.get('file_name', '')
        ret = excel_to_db(excel_file)
        if ret:
            smg = u'批量添加成功'
        else:
            emg = u'批量添加失败,请检查格式.'
    return my_render('jasset/asset_add_batch.html', locals(), request)



# tenant list add by Rain
@require_role('role')
def tenant_list(request):
    header_title, path1, path2 = u'查看租户', u'资产管理', u'查看租户'
    posts = Tenant_info.objects.all()
    conn = Q()
    q1 = Q()
    q1.connector = "OR"
    keyword = request.GET.get('keyword', '')
    env_type = request.GET.get('env_type','all')
    if keyword:
        coditions_list = ["tenant_name", "user_name", "user_passwd", "admin_host", "net_work", "comments"]
        for i in coditions_list:
            q1.children.append(("%s__icontains" % i, keyword))
        conn.add(q1, "AND")
    else:
        pass
    if env_type == 'all':
        posts = Tenant_info.objects.filter(conn)
    else:
        q2 = Q()
        q2.connector = "AND"
        q2.children.append(("env_type", env_type))
        conn.add(q2, "AND")
        posts = Tenant_info.objects.filter(conn)
    contact_list, p, contacts, page_range, current_page, show_first, show_end = pages(posts, request)
    return my_render('jasset/tenant_list.html',locals(),request)

@require_role('admin')
def tenant_add(request):
    """
    Tenant info  add view
    """
    header_title, path1, path2 = u'添加租户', u'资产管理', u'添加租户'
    if request.method == 'POST':
        tenant_form = TenantForm(request.POST)
        if tenant_form.is_valid():
            tenant_name = tenant_form.cleaned_data['tenant_name']
            if IDC.objects.filter(name=tenant_name):
                emg = u'添加租户失败, 此 %s 已存在!' % tenant_name
                return my_render('jasset/tenant_add.html', locals(), request)
            else:
                tenant_form.save()
                smg = u'IDC: %s添加成功' % tenant_name
            return HttpResponseRedirect(reverse('tenant_list'))
    else:
        Tenant_Form = TenantForm()
    return my_render('jasset/tenant_add.html', locals(), request)

@require_role('admin')
def tenant_del(request):
    """
    Tenant delete view
    """
    tenant_ids = request.GET.get('id', '')
    tenant_id_list = tenant_ids.split(',')
    for tenant_id in tenant_id_list:
        Tenant_info.objects.filter(id=tenant_id).delete()
    return HttpResponseRedirect(reverse('tenant_list'))

@require_role('admin')
def tenant_edit(request):
    """
    Tenant edit view
    """
    header_title, path1, path2 = u'编辑租户', u'资产管理', u'编辑租户'
    tenant_id = request.GET.get('id', '')
    tenant = get_object(Tenant_info, id=tenant_id)
    if request.method == 'POST':
        tenant_form  = TenantForm(request.POST, instance=tenant)
        if tenant_form.is_valid():
            tenant_form.save()
            return HttpResponseRedirect(reverse('tenant_list'))
    else:
        tenant_form = TenantForm(instance=tenant)
        print tenant_form
        return my_render('jasset/tenant_edit.html', locals(), request)

@require_role('admin')
def tenant_batch_add(requset):
    if requset.method == "POST":
        batch_info = requset.POST.get("batch_add",None)
        env_type =  requset.POST.get("env_type",None)
        print env_type
        if batch_info:
            for item in  batch_info.split(";"):
                if item =="":
                    continue
                try:
                    item =  item.strip().split("|")
                    tenant_obj = Tenant_info()
                    tenant_obj.tenant_name = item[0]
                    tenant_obj.user_name = item[1]
                    tenant_obj.user_passwd = item[2]
                    tenant_obj.admin_host = item[3]
                    tenant_obj.net_work = item[4]
                    tenant_obj.comments = item[5]
                    if env_type == "all":
                        tenant_obj.env_type = item[6]
                    else:
                        tenant_obj.env_type = env_type
                    tenant_obj.save()
                except Exception as e:
                    continue
    return HttpResponse("true")


@require_role('admin')
def tenant_tpl_add(request):
    if request.method == 'POST':
        try:
            excel_file = request.FILES.get('tpl_file', '')
            env_type = request.POST.get("env_type")
            data = xlrd.open_workbook(filename=None,file_contents=excel_file.read())
            table1 = data.sheets()[0]
            nrows = table1.nrows
            error_msg = ""
            for i in range(1, nrows):
                new_data = table1.row_values(i)
                print new_data
                new_tenant = Tenant_info()
                new_tenant.tenant_name = new_data[0]
                new_tenant.user_name = new_data[1]
                new_tenant.user_passwd = new_data[2]
                new_tenant.admin_host = new_data[3]
                new_tenant.net_work = new_data[4]
                new_tenant.env_type = env_type
                new_tenant.comments = new_data[5]
                new_tenant.save()

        except Exception as e:
            print e
            return HttpResponse("error")
        if error_msg!="":
            return HttpResponse(error_msg)
        return HttpResponse("true")


# @require_role('admin')
# def host_list(request):
#     header_title, path1, path2 = u'查看主机', u'资产管理', u'查看主机'
#     posts = Host_info.objects.all()
#     conn = Q()
#     q1 = Q()
#     q1.connector = "OR"
#     keyword = request.GET.get('keyword', '')
#     env_type = request.GET.get('env_type','all')
#     if keyword:
#         coditions_list = ["host_name", "host_ip", "host_user", "host_passwd", "SN", "comments"]
#         for i in coditions_list:
#             q1.children.append(("%s__icontains" % i, keyword))
#         conn.add(q1, "AND")
#     else:
#         pass
#     if env_type == 'all':
#         posts = Host_info.objects.select_related().filter(conn)
#     else:
#         q2 = Q()
#         q2.connector = "AND"
#         q2.children.append(("env_type", env_type))
#         conn.add(q2, "AND")
#         posts = Host_info.objects.select_related().filter(conn)
#     contact_list, p, contacts, page_range, current_page, show_first, show_end = pages(posts, request)
#     return my_render("jasset/host_list.html",locals(),request)
#
# @require_role('admin')
# def host_add(request):
#     """
#     host   add view
#     """
#     header_title, path1, path2 = u'添加主机', u'资产管理', u'添加主机'
#     if request.method == 'POST':
#         host_form = HostForm(request.POST)
#         idrac_form = IdracForm(request.POST)
#         # print idrac_form
#         # print host_form
#         if host_form.is_valid():
#             host_name = host_form.cleaned_data['host_name']
#             if Host_info.objects.filter(host_name=host_name):
#                 emg = u'添加主机失败, 此 %s 已存在!' % host_name
#                 return my_render('jasset/host_add.html', locals(), request)
#             else:
#                 host_model = host_form.save(commit=False)
#                 host_model.Idrac = idrac_form.save()
#                 host_model.save()
#                 smg = u'主机: %s添加成功' % host_name
#             return HttpResponseRedirect(reverse('host_list'))
#     else:
#         idrac_form = IdracForm()
#         host_form = HostForm()
#     return my_render('jasset/host_add.html', locals(), request)
#
# @require_role('admin')
# def del_host(host_id):
#     host = Host_info.objects.select_related().get(id=host_id)
#     idrac = host.Idrac
#     host.delete()
#     idrac.delete()
#
# @require_role('admin')
# def host_del(request):
#     """
#     Host delete view
#     """
#     hosts_ids = request.GET.get('id', '')
#     host_id_list = hosts_ids.split(',')
#     for host_id in host_id_list:
#         del_host(host_id)
#     return HttpResponseRedirect(reverse('host_list'))
#
# @require_role('admin')
# def host_edit(request):
#     """
#     Host edit view
#     """
#     header_title, path1, path2 = u'编辑主机', u'资产管理', u'编辑主机'
#     host_id = request.GET.get('id', '')
#     host = get_object(Host_info, id=host_id)
#     idrac = get_object(Idrac,id=host.Idrac.id)
#     if request.method == 'POST':
#         host_form  = HostForm(request.POST, instance=host)
#         idrac_form = IdracForm(request.POST,instance=idrac)
#         # print host_form
#         # print idrac_form
#         if all((host_form.is_valid(),idrac_form.is_valid())):
#             host_model = host_form.save(commit=False)
#             host_model.Idrac = idrac_form.save()
#             host_model.save()
#             return HttpResponseRedirect(reverse('host_list'))
#         else:
#             emg = "error"
#             return my_render('jasset/host_edit.html', locals(), request)
#     else:
#         host_form = HostForm(instance=host)
#         idrac_form = IdracForm(instance=idrac)
#         print host_form,idrac_form
#         return my_render('jasset/host_edit.html', locals(), request)
#
# @require_role('admin')
# def host_detail(request):
#     host_id = request.GET.get('id',"")
#     host = get_object(Host_info,id=host_id)
#     header_title, path1, path2 = u'主机详细内容', u'资产管理', u'%s详细内容'%host.host_name
#     return  my_render('jasset/host_detail.html',locals(),request)
#
# @require_role('admin')
# def host_batch_add(request):
#     if request.method == "POST":
#         batch_info = request.POST.get("batch_add",None)
#         env_type =  request.POST.get("env_type",None)
#         print env_type,batch_info
#         if batch_info:
#             for item in  batch_info.split(";"):
#                 if item =="":
#                     continue
#                 try:
#                     item =  item.strip().split("|")
#                     new_host = Host_info()
#                     new_host.host_name=item[0]
#                     new_host.SN = item[1]
#                     new_host.host_ip = item[2]
#                     new_host.host_models = item[3]
#                     new_host.comments = item[4]
#                     new_idrac = Idrac()
#                     new_idrac.Idrac_ip = item[5]
#                     new_idrac.Idrac_user = item[6]
#                     new_idrac.Idrac_passwd = item[7]
#                     new_idrac.save()
#                     new_host.Idrac = new_idrac
#                     new_host.env_type = env_type
#                     new_host.save()
#                     if env_type == "all":
#                         new_host.env_type = item[6]
#                     else:
#                         new_host.env_type = env_type
#                     new_host.save()
#                 except Exception as e:
#                     continue
#     return HttpResponse("true")


@require_role('admin')
def host_tpl_add(request):
    if request.method == 'POST':
        try:
            excel_file = request.FILES.get('tpl_file', '')
            env_type = request.POST.get("env_type")
            data = xlrd.open_workbook(filename=None,file_contents=excel_file.read())
            table1 = data.sheets()[0]
            nrows = table1.nrows
            error_msg = ""
            for i in range(1, nrows):
                new_data = table1.row_values(i)
                print new_data
                new_host = Host_info()
                new_host.env_type = env_type
                new_host.host_ip = new_data[0]
                new_host.host_name = new_data[1]
                new_host.host_user = new_data[2]
                new_host.host_passwd = new_data[3]
                new_host.host_models = new_data[4]
                new_host.comments = new_data[5]
                new_host.SN = new_data[6]
                new_idrac = Idrac()
                new_idrac.Idrac_ip = new_data[7]
                new_idrac.Idrac_user = new_data[8]
                new_idrac.Idrac_passwd = new_data[9]
                new_idrac.save()
                new_host.Idrac = new_idrac
                new_host.save()

        except Exception as e:
            print e
            return HttpResponse("error")
        if error_msg!="":
            return HttpResponse(error_msg)
        return HttpResponse("true")

@require_role('admin')
def url_list(request):
    header_title, path1, path2 = u'查看URL', u'资产管理', u'查看URL'
    posts = Url_info.objects.all()
    conn = Q()
    q1 = Q()
    q1.connector = "OR"
    keyword = request.GET.get('keyword', '')
    env_type = request.GET.get('env_type', 'all')
    if keyword:
        coditions_list = ["url", "server_name", "user_name", "user_passwd", "host_type", "comments"]
        for i in coditions_list:
            q1.children.append(("%s__icontains" % i, keyword))
        conn.add(q1, "AND")
    else:
        pass
    if env_type == 'all':
        posts = Url_info.objects.filter(conn)
    else:
        q2 = Q()
        q2.connector = "AND"
        q2.children.append(("env_type", env_type))
        conn.add(q2, "AND")
        posts = Url_info.objects.filter(conn)
    contact_list, p, contacts, page_range, current_page, show_first, show_end = pages(posts, request)
    return my_render("jasset/url_list.html", locals(), request)

@require_role('admin')
def url_add(request):
    """
    Url   add view
    """
    header_title, path1, path2 = u'添加URL', u'资产管理', u'添加URL'
    if request.method == 'POST':
        url_form = UrlForm(request.POST)

        if url_form.is_valid():
            url = url_form.cleaned_data['url']
            if Url_info.objects.filter(url=url):
                emg = u'添加URL失败, 此 %s 已存在!' % url
                return my_render('jasset/url_add.html', locals(), request)
            else:
                url_form.save()
                smg = u'URL: %s添加成功' % url
            return HttpResponseRedirect(reverse('url_list'))
    else:
        url_form = UrlForm()
    return my_render('jasset/url_add.html', locals(), request)


@require_role('admin')
def url_del(request):
    """
    URL delete view
    """
    urls_ids = request.GET.get('id', '')
    url_id_list = urls_ids.split(',')
    for url_id in url_id_list:
        Url_info.objects.filter(id=url_id).delete()
    return HttpResponseRedirect(reverse('url_list'))


@require_role('admin')
def url_edit(request):
    """
    Url  edit view
    """
    header_title, path1, path2 = u'编辑URL', u'资产管理', u'编辑URL'
    url_id = request.GET.get('id', '')
    url = get_object(Url_info, id=url_id)
    if request.method == 'POST':
        url_form  = UrlForm(request.POST, instance=url)

        if url_form.is_valid():
            url_form.save()
            return HttpResponseRedirect(reverse('url_list'))
        else:
            emg = "error"
            return my_render('jasset/url_edit.html', locals(), request)
    else:
        url_form = UrlForm(instance=url)
        print url_form
        return my_render('jasset/url_edit.html', locals(), request)

@require_role('admin')
def url_tpl_add(request):
    if request.method == 'POST':
        try:
            excel_file = request.FILES.get('tpl_file', '')
            env_type = request.POST.get("env_type")
            data = xlrd.open_workbook(filename=None,file_contents=excel_file.read())
            table1 = data.sheets()[0]
            nrows = table1.nrows
            error_msg = ""
            for i in range(1, nrows):
                new_data = table1.row_values(i)
                print new_data
                new_url = Url_info()
                new_url.url = new_data[0]
                new_url.env_type = new_data[1]
                new_url.server_name = new_data[2]
                new_url.user_name = new_data[3]
                new_url.user_passwd = new_data[4]
                new_url.host_type = new_data[5]
                new_url.comments = new_data[6]
                new_url.save()
        except Exception as e:
            print e
            return HttpResponse("error")
        if error_msg != "":
            return HttpResponse(error_msg)
        return HttpResponse("true")


@require_role('admin')
def virtual_platform_list(request):
    header_title, path1, path2 = u'查看虚拟化平台', u'资产管理', u'查看虚拟化平台'
    posts = Virtual_platform.objects.all()
    conn = Q()
    q1 = Q()
    q1.connector = "OR"
    keyword = request.GET.get('keyword', '')
    virtual_type = request.GET.get('virtual_type', 'all')
    if keyword:
        coditions_list = ["platform_name", "zone", "host_info__host_name", "host_info__host_ip","host_info__comments"]
        for i in coditions_list:
            q1.children.append(("%s__icontains" % i, keyword))
        conn.add(q1, "AND")
    else:
        pass
    if virtual_type == 'all':
        posts = Virtual_platform.objects.select_related().filter(conn)
    else:
        q2 = Q()
        q2.connector = "AND"
        q2.children.append(("virtual_type", virtual_type))
        conn.add(q2, "AND")
        posts = Virtual_platform.objects.select_related().filter(conn)
    contact_list, p, contacts, page_range, current_page, show_first, show_end = pages(posts, request)
    return my_render("jasset/Virtual_platform.html", locals(), request)

@require_role('admin')
def virtual_platform_detail(request):
    if request.method == "GET":
        conn = Q()
        q1 = Q()
        q1.connector = "OR"
        keyword = request.GET.get('keyword', '')
        if keyword:
            coditions_list = ["host_ip", "host_name", "host_comments"]
            for i in coditions_list:
                q1.children.append(("%s__icontains" % i, keyword))
            conn.add(q1, "AND")
        else:
            pass
        platform_id = request.GET.get('id',"")
        platform = get_object(Virtual_platform,id=platform_id)
        q2 = Q()
        q2.connector = "AND"
        q2.children.append(("server", platform))
        conn.add(q2, "AND")
        virtual_host_form = VirtualHostForm()
        header_title, path1, path2 = u'虚拟化平台详细内容', u'资产管理', u'%s详细内容'%platform.platform_name
        posts = Virtual_host.objects.select_related().filter(conn)
        contact_list, p, contacts, page_range, current_page, show_first, show_end = pages(posts, request)
        return  my_render('jasset/virtual_platform_detail.html',locals(),request)
    else:
        # add new virtual host in platform
        platform_id = request.POST.get("id")
        virtual_host_form = VirtualHostForm(request.POST)
        virtual_host_model = virtual_host_form.save(commit=False)
        virtual_host_model.server = Virtual_platform.objects.get(id=platform_id)
        virtual_host_model.save()
        return HttpResponse("true")

@require_role('admin')
def virtual_platform_add(request):
    """
    virtual_platform   add view
    """
    header_title, path1, path2 = u'添加虚拟化平台', u'资产管理', u'添加虚拟化平台'
    if request.method == 'POST':
        platform_form  = VirtualForm(request.POST)
        host_form = AssetForm(request.POST)
        idrac_form = IdracForm(request.POST)
        # print platform_form
        # print host_form
        # print idrac_form
        if all((platform_form.is_valid(), host_form.is_valid()) ):
        #
        # if platform_form.is_valid():
            platform_name = platform_form.cleaned_data['platform_name']
            if Virtual_platform.objects.filter(platform_name=platform_name):
                emg = u'添加虚拟化平台失败, 此 %s 已存在!' % platform_name
                return my_render('jasset/virtual_platform_add.html', locals(), request)
            else:
                platform_model =platform_form.save(commit=False)
                host_model = host_form.save(commit=False)
                if idrac_form.is_valid():
                    host_model.remote_ip = idrac_form.save()
                host_model.env = 4
                host_model.save()
                platform_model.host_info = host_model
                platform_model.save()
                smg = u'虚拟化平台: %s添加成功' % platform_name
            return HttpResponseRedirect(reverse('virtual_platform_list'))
    else:
        platform_form = VirtualForm()
        host_form = AssetForm()
        idrac_form = IdracForm()
    return my_render('jasset/virtual_platform_add.html', locals(), request)


@require_role('admin')
def virtual_platform_del(request):
    """
    virtual_platform delete view
    """
    platform_ids = request.GET.get('id', '')
    platform_id_list = platform_ids.split(',')
    for platform_id in platform_id_list:
        platform = Virtual_platform.objects.select_related().get(id=platform_id)
        platform.delete()
        Asset.objects.get(id=platform.host_info_id).delete()
    return HttpResponseRedirect(reverse('asset_list'))


@require_role('admin')
def virtual_platform_edit(request):
    """
    virtual_platform edit view
    """
    header_title, path1, path2 = u'编辑平台', u'资产管理', u'编辑平台'
    platform_id = request.GET.get('id', '')
    platform = get_object(Virtual_platform, id=platform_id)
    host = get_object(Host_info,id=platform.host_info.id)
    idrac = get_object(Idrac,id=host.Idrac.id)
    if request.method == 'POST':
        platform_form = VirtualForm(request.POST,instance=platform)
        host_form  = HostForm(request.POST, instance=host)
        idrac_form = IdracForm(request.POST,instance=idrac)
        # print host_form
        # print idrac_form
        if all((platform_form.is_valid(),host_form.is_valid(),idrac_form.is_valid())):
            platform_model = platform_form.save(commit=False)
            host_model = host_form.save(commit=False)
            host_model.Idrac = idrac_form.save()
            host_model.env_type = "virtual"
            host_model.save()
            platform_model.host_info = host_model
            platform_model.save()
            return HttpResponseRedirect(reverse('virtual_platform_list'))
        else:
            emg = "error"
            return my_render('jasset/virtual_platform_edit.html', locals(), request)
    else:
        platform_form = VirtualForm(instance=platform)
        host_form = HostForm(instance=host)
        idrac_form = IdracForm(instance=idrac)
        print host_form,idrac_form
        return my_render('jasset/virtual_platform_edit.html', locals(), request)


@require_role('admin')
def virtual_host_del(request):
    virtual_host_ids = request.GET.get('id', '')
    virtual_host_id_list = virtual_host_ids.split(',')
    for virtual_host_id in virtual_host_id_list:
        Virtual_host.objects.filter(id=virtual_host_id).delete()
    return HttpResponse("true")

@require_role('admin')
def virtual_host_edit(request):
    """
    virtual_host  edit view
    """
    header_title, path1, path2 = u'修改虚拟主机', u'资产管理', u'修改虚拟主机'
    platform_id = request.GET.get("platform_id")
    virtual_host_id = request.GET.get('id', '')
    virtual_host = get_object(Virtual_host, id=virtual_host_id)
    if request.method == 'POST':
        virtual_host_form  = VirtualHostForm(request.POST, instance=virtual_host)

        if virtual_host_form.is_valid():
            virtual_host_form.save()
            return HttpResponseRedirect(reverse('virtual_platform_detail')+"?id="+platform_id)
        else:
            emg = "error"
            return my_render('jasset/virtual_host_edit.html', locals(), request)
    else:
        print platform_id
        virtual_host_form = VirtualHostForm(instance=virtual_host)
        print virtual_host_form
        return my_render('jasset/virtual_host_edit.html', locals(), request)

@require_role('admin')
def batch_add_virtual_host(request):
    if request.method == "POST":
        batch_info = request.POST.get("batch_add",None)
        platform_id = request.POST.get("platform_id")
        # print  platform_id
        platform = Virtual_platform.objects.get(id=platform_id)
        # print batch_info
        if batch_info:
            for item in  batch_info.split(";"):
                if item =="":
                    continue
                try:
                    item =  item.strip().split("|")
                    print item
                    new_host = Virtual_host()
                    new_host.host_ip=item[0]
                    new_host.host_name=item[1]
                    new_host.host_comments=item[2]
                    new_host.server=platform
                    new_host.save()
                except Exception as e:
                    print e
                    continue
    return HttpResponse("true")