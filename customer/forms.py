from django import forms


class LoginForm(forms.Form):
    #通过 widget 参数，我们设置了这个字段在 HTML 中渲染的方式，即渲染为一个 'input' 元素
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        #样式类 'form-control'，占位符 'Username'，以及让这个字段自动获取焦点；
        # error_messages 参数用来自定义验证错误的消息，以字典的形式提供；
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}),
                               error_messages={'required': '用户名不能为空', 'min_length': '用户名最少为3个字符',
                                               'max_length': '用户名最不超过为20个字符'}, )
    password = forms.CharField(label="密码", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password1 = forms.CharField(label="密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    tel = forms.CharField(label="电话", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "TEL"}))


class AddressForm(forms.Form):
    customer_address = forms.CharField(label="联系人地址", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "customer_address", 'autofocus': ''}),required=False)
    customer_company = forms.CharField(label="公司名称", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "customer_company", 'autofocus': ''}),required=False)
    customer_job = forms.CharField(label="联系人职业", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "customer_job", 'autofocus': ''}),required=False)
    customer_city = forms.CharField(label="城市", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "customer_city", 'autofocus': ''}),required=False)

    CHOICES = [(0, '华北'), (1, '东北'), (2, '华东'), (3, '华西'), (4, '华中'), (5, '华南'), (6, '西南'), (7, '西北')]
    customer_area = forms.ChoiceField(label="地区", choices=CHOICES,
                                      widget=forms.Select(attrs={'class': 'form-control','placeholder': "customer_area", 'autofocus': ''}), required=False)
    customer_postalcode = forms.CharField(label="邮政编码", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "customer_postalcode", 'autofocus': ''}),required=False)
    customer_fax = forms.CharField(label="传真", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "customer_fax", 'autofocus': ''}),required=False)
    customer_country = forms.CharField(label="国家", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "customer_country", 'autofocus': ''}),required=False)
