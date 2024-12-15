from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, AddressForm
from django.contrib import messages
from .models import Customer, Address
def register(request):
    # 创建一个空的注册表单实例
    register_form = RegisterForm()
    if request.session.get('is_login', None):
        return render(request, 'customer/index.html', locals())  # 自动跳转到首页
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            tel = register_form.cleaned_data['tel']

            if password1 != password2:
                print("[DEBUG][POST][STATE]:两次输入的密码不同！")
                return render(request, 'customer/register.html', locals())
            else:
                same_id_cus = Customer.objects.filter(customer_name=username)
                if same_id_cus:
                    message = '顾客用户名已经存在~请换一个'
                    return render(request, 'customer/register.html', locals())
                # 当一切都OK的情况下，创建新用户
                else:
                    new_cus = Customer.objects.create(customer_name=username, customer_tel=tel,
                                                      customer_password=password1)
                    new_cus.save()
                    # 自动跳转到登录页面
                    login_form = LoginForm()
                    message = "注册成功！"
                    return render(request, 'customer/login.html', locals())  # 自动跳转到登录页面
    else:
        return render(request, 'customer/register.html', locals())

    return render(request, 'customer/register.html', locals())


def login(request):
    login_form = LoginForm()
    if request.session.get('is_login', None):
        print("[DEBUG][POST][STATE]:已经登陆")
        return render(request, 'customer/index.html', locals())

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print("[DEBUG][POST][LOGIN][username]:{}".format(username))
            print("[DEBUG][POST][LOGIN][password]:{}".format(password))
            try:
                print("[DEBUG][POST][STATE]:查询顾客用户数据库")
                user_cus = Customer.objects.get(customer_name=username)
                if user_cus.customer_password == password:
                    print("[DEBUG][POST][USERNAME]:{}".format(user_cus.customer_name))
                    print("[DEBUG][POST][STATE]:登录成功")
                    messages.success(request, '{}登录成功！'.format(user_cus.customer_name))
                    user_cus.customer_status = 1
                    user_cus.save()
                    request.session['is_login'] = True
                    request.session['user_id'] = user_cus.customer_id
                    request.session['user_name'] = user_cus.customer_name
                    return render(request, 'customer/index.html', locals())
                else:
                    print("[DEBUG][POST][STATE]:密码不正确")
                    message = "密码不正确"
            except:
                print("[DEBUG][POST][STATE]:用户不存在")
                message = "用户不存在"
    return render(request, 'customer/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return render(request, 'customer/index.html', locals())
    user_id = request.session['user_id']
    print("[DEBUG][REQUEST][退出]]")
    print("[DEBUG][REQUEST][USER_ID]:{}".format(user_id))
    try:
        user = Customer.objects.get(customer_id=user_id)
        print("[DEBUG][REQUEST][退出]]：退出顾客身份")
        user.customer_status = 0  # 更新离线状态
        user.save()
    except:
        print("[DEBUG][request][STATE]:退出错误，无法更新数据库中用户状态")

    request.session.flush()
    return render(request, 'customer/index.html', locals())


def information(request):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')
    area_dict = {0: '华北', 1: '东北', 2: '华东', 3: '华西', 4: '华中', 5: '华南', 6: '西南', 7: '西北'}
    address_form = AddressForm()
    customer_id = request.session['user_id']
    customer = Customer.objects.filter(customer_id=customer_id).first()

    if customer.address:
        print("已经填过地址")
        return redirect("customer:show_info")

    if request.method == "POST":
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            new_customer_address = address_form.cleaned_data['customer_address']
            new_customer_company = address_form.cleaned_data['customer_company']
            new_customer_job = address_form.cleaned_data['customer_job']
            new_customer_city = address_form.cleaned_data['customer_city']
            new_customer_area = int(address_form.cleaned_data['customer_area'])
            new_customer_postalcode = address_form.cleaned_data['customer_postalcode']
            new_customer_fax = address_form.cleaned_data['customer_fax']
            new_customer_country = address_form.cleaned_data['customer_country']

            try:
                cus_info = Address.objects.create(customer_address=new_customer_address,
                                                  customer_company=new_customer_company, customer_job=new_customer_job,
                                                  customer_city=new_customer_city, customer_area=new_customer_area,
                                                  customer_postalcode=new_customer_postalcode,
                                                  customer_fax=new_customer_fax, customer_country=new_customer_country)
                cus_info.save()
                customer = Customer.objects.filter(customer_id=customer_id).first()
                customer.address = cus_info
                customer.save()
                messages.success(request, '个人地址添加成功!')
                return redirect('customer:show_info')
            except Exception as e:
                print(e)
                messages.warning(request, '个人地址添加失败!')
                return render(request, 'customer/information.html', locals())

    return render(request, 'customer/information.html', locals())


def show_info(request):
    customer_id = request.session['user_id']
    customer = Customer.objects.filter(customer_id=customer_id).first()
    area_dict = {0: '华北', 1: '东北', 2: '华东', 3: '华西', 4: '华中', 5: '华南', 6: '西南', 7: '西北'}
    context = {
        'user_name': request.session['user_name'],
        'customer_address': customer.address.customer_address,
        'customer_company': customer.address.customer_company,
        'customer_city': customer.address.customer_city,
        'customer_area': area_dict[customer.address.customer_area],
        'customer_postalcode': customer.address.customer_postalcode,
        'customer_fax': customer.address.customer_fax,
        'customer_country': customer.address.customer_country,
    }

    return render(request, 'customer/show_info.html', context)


def edit_info(request):
    customer_id = request.session['user_id']
    customer = Customer.objects.filter(customer_id=customer_id).first()
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            customer.address.customer_address = address_form.cleaned_data['customer_address']
            customer.address.customer_company = address_form.cleaned_data['customer_company']
            customer.address.customer_job = address_form.cleaned_data['customer_job']
            customer.address.customer_city = address_form.cleaned_data['customer_city']
            customer.address.customer_area = int(address_form.cleaned_data['customer_area'])
            customer.address.customer_postalcode = address_form.cleaned_data['customer_postalcode']
            customer.address.customer_fax = address_form.cleaned_data['customer_fax']
            customer.address.customer_country = address_form.cleaned_data['customer_country']
            customer.address.save()
            messages.success(request, '个人地址编辑成功!')
            return redirect('customer:show_info')
    else:
        initial_data = {
            'customer_address': customer.address.customer_address,
            'customer_company': customer.address.customer_company,
            'customer_job': customer.address.customer_job,
            'customer_city': customer.address.customer_city,
            'customer_area': customer.address.customer_area,
            'customer_postalcode': customer.address.customer_postalcode,
            'customer_fax': customer.address.customer_fax,
            'customer_country': customer.address.customer_country,
        }
        address_form = AddressForm(initial=initial_data)  # 初始化表单数据
    context = {'address_form': address_form}
    return render(request, 'customer/edit_info.html', context)
