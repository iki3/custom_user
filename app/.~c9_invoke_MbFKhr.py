from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, resolve_url
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import generic
from .forms import (
    LoginForm, UserCreateForm, UserUpdateForm, MyPasswordChangeForm,
    MyPasswordResetForm, MySetPasswordForm,searchForm
)

from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from .models import InfoModelForm
from .forms import InfoModelFormAdd

from django.http.response import JsonResponse
import os
module_dir = os.path.dirname(__file__) # views.pyのあるディレクトリを取得
json_path = os.path.join(module_dir, 'hoge.json')
from django.http import HttpResponse,Http404

import json
import logging
import re

#from app/json import hoge.js


User = get_user_model()
Userq=User

class Top(generic.TemplateView):
    template_name = 'app_templates/top.html'


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'app_templates/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'app_templates/top.html'
def map(request):
    return render(request, 'app_templates/map.html')
    
def info(request):
    infodata = InfoModelForm.objects.all()
    header = ['ID','名前','メール','性別','部署','社歴','作成日']
    my_dict2 = {
        'title':'テスト',
        'val':infodata,
        'header':header
    }
    f = open('/home/ec2-user/environment/english_test/app/static/app/json/hoge.json', 'r')
    json_dict = json.load(f)
    print(json_dict['lat'])
    
 

    return render(request, 'app_templates/info.html',my_dict2)

def create(request):
   

    if (request.method == 'POST'):
        obj = InfoModelForm()
        info = InfoModelFormAdd(request.POST,instance=obj)
        info.save()
        return redirect(to='/info')
    modelform_dict = {
        'title':'modelformテスト',
        'form':InfoModelFormAdd(),
    }
    return render(request, 'app_templates/create.html',modelform_dict)
    
def ajax(request):
    logger = logging.getLogger('development')
    print('Hello World!')
    return render(request,'app_templates/surprise.html')
    
    
    
    
    
def for_ajax(request):    # AJAXに答える関数


    if request.method == 'POST':
        txt = request.POST['your_txt']  # POSTデータを取得して
        surprise_txt = txt + "!!!"  # 加工
        print("こんにちは")
        print (txt)
        response = json.dumps({'your_surprise_txt':surprise_txt,})  # JSON形式に直して・・

        return HttpResponse(response,content_type='application/json')  # 返す。JSONはjavascript扱いなのか・・

    else:
        print("こんばんわ")
        raise Http404  # GETリクエストを404扱いにしているが、実際は別にしなくてもいいかも   

def map1(request):
    logger = logging.getLogger('development')
    print('Hello World!')
    return render(request,'app_templates/map1.html')
    
def map2(request):    # AJAXに答える関数


    if request.method == 'POST':
        txt = request.POST['lat'] # POSTデータを取得して
        txt2=request.POST['lng']
     #   print('book1の情報：{}'.format(txt['lat']))
     #  print('book1の情報：{}'.format(txt['lng']))
     #   surprise_txt = format(txt['lat'])+ "!!!"  # 加工
        print("こんにちは")
        print (txt)
        print (txt2)
        print(type(txt))
        surprise_txt = txt + "!!!" 
  #      moji=txt.rsplit('}')[0]
   #     moji = txt.split('{')[0]
        my_dict2 = {
           'lat':txt,
           'lng':txt2,
        }
     #   print(moji)
     #   response = txt # JSON形式に直して・・
        response = json.dumps({'your_surprise_txt':surprise_txt,})
        
        f2 = open('/home/ec2-user/environment/english_test/app/static/app/json/hoge.json', 'w')
        json.dump(my_dict2, f2)
        f = open('/home/ec2-user/environment/english_test/app/static/app/json/hoge.json', 'r')
   #     json_dict = json.load(f)
#        txt3=f['lat']
  #      print (json_dict)
        
        return HttpResponse(response,content_type='application/javascript')  # 返す。JSONはjavascript扱いなのか・・

    else:
        print("こんばんわ")
        raise Http404  # GETリクエストを404扱いにしているが、実際は別にしなくてもいいかも   


def save_latlng(request):    # AJAXに答える関数


    if request.method == 'POST':
        txt = request.POST['lat'] # POSTデータを取得して
        txt2=request.POST['lng']
     #   print('book1の情報：{}'.format(txt['lat']))
     #  print('book1の情報：{}'.format(txt['lng']))
     #   surprise_txt = format(txt['lat'])+ "!!!"  # 加工
    #   print (txt)
     #   print (txt2)
     #   print(type(txt))
        surprise_txt = txt + "!!!" 
  #      moji=txt.rsplit('}')[0]
   #     moji = txt.split('{')[0]
        my_dict2 = {
           'lat':txt,
           'lng':txt2,
        }
     #   print(moji)
     #   response = txt # JSON形式に直して・・
        response = json.dumps({'your_surprise_txt':surprise_txt,})
        
    #    f2 = open('/home/ec2-user/environment/english_test/app/static/app/json/hoge.json', 'w')
    #    json.dump(my_dict2, f2)
    #    f = open('/home/ec2-user/environment/english_test/app/static/app/json/hoge.json', 'r')
   #     json_dict = json.load(f)
#        txt3=f['lat']
  #      print (json_dict)
        U=Userq.objects.get(pk=2)
        U.example3=txt+":"+txt2
        U.save()
        return HttpResponse(response,content_type='application/javascript')  # 返す。JSONはjavascript扱いなのか・・

    else:
        print("こんばんわ")
        raise Http404  # GETリクエストを404扱いにしているが、実際は別にしなくてもいいかも   













   
    
class UserCreate(generic.CreateView):
    """ユーザー仮登録"""
    template_name = 'app_templates/user_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        
        """仮登録と本登録用メールの発行."""
        # 仮登録と本登録の切り替えは、is_active属性を使うと簡単です。
        # 退会処理も、is_activeをFalseにするだけにしておくと捗ります。
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # アクティベーションURLの送付
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': 'https' if self.request.is_secure() else 'http',
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }
        subject_template = get_template('app_templates/mail_template/create/subject.txt')
        subject = subject_template.render(context)

        message_template = get_template('app_templates/mail_template/create/message.txt')
        message = message_template.render(context)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.username]
        send_mail(subject, message, from_email, recipient_list)
        return redirect('app:user_create_done')
        
        
        


def mailmail(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['yojironoda1@gmail.com']
    send_mail( subject, message, email_from, recipient_list,)
#    return redirect('redirect to a new page')
#    send_mail('Subject here','Here is the message.','ryuseisoccer2@gmail.com',['yojironoda1@gmail.com'],)
    return render(request, 'app_templates/index.html')
#    

class UserCreateDone(generic.TemplateView):
    """ユーザー仮登録したよ"""
    template_name = 'app_templates/user_create_done.html'


class UserCreateComplete(generic.TemplateView):
    """メール内URLアクセス後のユーザー本登録"""
    template_name = 'app_templates/user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)  # デフォルトでは1日以内

    def get(self, request, **kwargs):
        """tokenが正しければ本登録."""
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        # 期限切れ
        except SignatureExpired:
            return HttpResponseBadRequest()

        # tokenが間違っている
        except BadSignature:
            return HttpResponseBadRequest()

        # tokenは問題なし
        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoenNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    # まだ仮登録で、他に問題なければ本登録とする
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()


class OnlyYouMixin(UserPassesTestMixin):
    """本人か、スーパーユーザーだけユーザーページアクセスを許可する"""
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class UserDetail(OnlyYouMixin, generic.DetailView):
    """ユーザーの詳細ページ"""
    model = Userq
    template_name = 'app_templates/user_detail.html'  # デフォルトユーザーを使う場合に備え、きちんとtemplate名を書く


class UserUpdate(OnlyYouMixin, generic.UpdateView):
    """ユーザー情報更新ページ"""
    model = Userq
    form_class = UserUpdateForm
    template_name = 'app_templates/user_form.html'  # デフォルトユーザーを使う場合に備え、きちんとtemplate名を書く

    def get_success_url(self):
        return resolve_url('app:user_detail', pk=self.kwargs['pk'])


class PasswordChange(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('app:password_change_done')
    template_name = 'app_templates/password_change.html'


class PasswordChangeDone(PasswordChangeDoneView):
    """パスワード変更しました"""
    template_name = 'app_templates/password_change_done.html'


class PasswordReset(PasswordResetView):
    """パスワード変更用URLの送付ページ"""
    subject_template_name = 'app_templates/mail_template/password_reset/subject.txt'
    email_template_name = 'app_templates/mail_template/password_reset/message.txt'
    template_name = 'app_templates/password_reset_form.html'
    form_class = MyPasswordResetForm
    success_url = reverse_lazy('app:password_reset_done')


class PasswordResetDone(PasswordResetDoneView):
    """パスワード変更用URLを送りましたページ"""
    template_name = 'app_templates/password_reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    """新パスワード入力ページ"""
    form_class = MySetPasswordForm
    success_url = reverse_lazy('app:password_reset_complete')
    template_name = 'app_templates/password_reset_confirm.html'


class PasswordResetComplete(PasswordResetCompleteView):
    """新パスワード設定しましたページ"""
    template_name = 'app_templates/password_reset_complete.html'



# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = "https://www.googleapis.com/auth/gmail.send"
CLIENT_SECRET_FILE = "client_secret.json"
APPLICATION_NAME = "MyGmailSender"
