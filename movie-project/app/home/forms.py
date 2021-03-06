# coding:utf8
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField,StringField,PasswordField,FileField,TextAreaField
from wtforms.validators import DataRequired,EqualTo,Email,Regexp,ValidationError
from app.modules import User

class RegisterForm(FlaskForm):
    """会员注册表单"""
    name = StringField(
        label="昵称",
        validators=[
            DataRequired("请输入昵称")
        ],
        description="昵称",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入昵称！",
            # "required": 'required'
        }
    )
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("请输入邮箱"),
            Email("邮箱格式不正确")
        ],
        description="邮箱",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！",
            # "required": 'required'
        }
    )
    phone = StringField(
        label="手机",
        validators=[
            DataRequired("请输入手机号"),
            Regexp("1[3458]\d{9}",message="手机格式不正确")
        ],
        description="手机",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机号！"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！"
        }
    )
    repwd = PasswordField(
        label="请再次输入密码",
        validators=[
            DataRequired("请再次输入密码"),
            EqualTo('pwd','两次输入密码不一致')
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请再次输入密码！"
        }
    )
    submit = SubmitField(
        '注册',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

    def validate_name(self,field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError("昵称已存在")

    def validate_email(self,field):
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError("邮箱已存在")

    def validate_phone(self,field):
        phone = field.data
        user = User.query.filter_by(phone=phone).count()
        if user == 1:
            raise ValidationError("手机号已存在")

class LoginForm(FlaskForm):
    name = StringField(
        label="账号",
        validators=[
            DataRequired("请输入账号")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！"
        }
    )
    submit = SubmitField(
        '登陆',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

class UserDetailForm(FlaskForm):
    name = StringField(
        label="账号",
        validators=[
            DataRequired("请输入账号")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！"
        }
    )
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("请输入邮箱"),
            Email("邮箱格式不正确")
        ],
        description="邮箱",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！",
            # "required": 'required'
        }
    )
    phone = StringField(
        label="手机",
        validators=[
            DataRequired("请输入手机号"),
            Regexp("1[3458]\d{9}", message="手机格式不正确")
        ],
        description="手机",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机号！"
        }
    )
    face = FileField(
        label="文件",
        validators=[
            DataRequired("请上传文件！")
        ],
        description="文件",
    )
    info = TextAreaField(
        label="简介",
        validators=[
            DataRequired("请输入简介！")
        ],
        description="片名",
        render_kw={
            "class": "form-control",
            "row": "10!"
        }
    )
    submit = SubmitField(
        '保存修改',
        render_kw={
            "class": "btn btn-success btn-block btn-flat"
        }
    )