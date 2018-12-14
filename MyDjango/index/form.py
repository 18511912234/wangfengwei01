#编写表单的实现功能

from django import forms
from .models import *
from django.core.exceptions import ValidationError

#自定义数据验证函数
def weight_validate(value):
    if not str(value).isdigit():
        raise ValidationError('请输入正确的重量')

#表单
class ProductForm(forms.Form):
    name=forms.CharField(max_length=20,label="名字",widget=forms.widgets.TextInput(attrs={'class':'c1'}),error_messages={'required':'名字不能未空'})
    weight=forms.CharField(max_length=20,label="重量",validators=[weight_validate])
    size=forms.CharField(max_length=20,label="尺寸")


    #获取数据库数据
    choices_list=[(i,v['type_name']) for i,v in enumerate(Type.objects.values('type_name'))]

    #设置css样式
    type = forms.ChoiceField(widget=forms.widgets.Select(attrs={'class':'type','siz qsd 7e':'4'}),choices=choices_list, label="产品类型")

class ProductModelForm(forms.ModelForm):
    productId=forms.CharField(max_length=20,label="产品序号")
    class Meta:
        #绑定模型
        model=Product
        #这几个字段转换成表单
        fields=['name','weight','size','type']
        #这里面的字段禁止转换成表单
        exclude=[]
        #设置lable标签
        labels={
            'name':'产品名称',
            'weight':'重量',
            'size':'尺寸',
            'tyoe':'产品类型'
        }

        # 定义表单字段的css样式
        widgets={
            'name':forms.widgets.TextInput(attrs={'class':'c1'}),
        }

        #定义字段类型
        field_classes={
            'name':''
        }

        error_messages={
            '__all__':{'required':'请输入内容',
                       'invalid':'请检查输入内容'},
            'weight':{'required':'请输入重量数值',
                       'invalid':'请检查数值的正确性'

            }
        }
    def clean_weight(self):
        data=self.cleaned_data['weight']
        return data+'g'