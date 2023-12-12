from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password,make_password
from rest_framework.response import Response
from testApp.models import products,user_cred,card,address
# Create your views here.
def create(reques):
    return HttpResponse("hello")

@api_view(['POST'])
def create_product(request,format=None):
    title_input=request.data['title']
    price_input=request.data['price']
    category_input=request.data['category']
    desc_input=request.data['desc']
    image_input=request.data['image']
 
   
    obj=products(
        title=title_input,
        price=price_input,
        category=category_input,
        desc=desc_input,
        image=image_input
    )
    obj.save()
    return Response({'message':'product successfully'})


@api_view(['GET'])
def get_product(request,format=None):
    all=products.objects.all().values()
    return Response({'all_products':all})

@api_view(['POST'])
def create_user(request,format=None):
    name_input=request.data['name']
    email_input=request.data['email']
    phone_input=request.data['phone']
    password_input=request.data['password']
    obj=user_cred(
        name=name_input,
        email=email_input,
        phone=phone_input,
        password=make_password(password_input)
    )
    obj.save()
    return Response({'message':'Successfully Registered'})


@api_view(['POST'])
def login(request, format=None):
    email_input = request.data.get('email')
    password = request.data.get('password')
    try:
        user_get=user_cred.objects.get(email=email_input)
    except:
        return Response({'message':'user does not found'})
    #print(user_get.password)
    if(check_password(password,user_get.password)):
        return Response({'status':'successfull loged in'})
                    
    else:
        return Response({'status':'password doesnot match'})
@api_view(["GET"])
def get_user(request):
    obj=user_cred.objects.all().values()
    return Response({"objects":obj})


@api_view(['POST'])
def create_card(request,format=None):
    idProduct_input=request.data['productId']
    email_input=request.data['email']
    title_input=request.data['title']
    price_input=request.data['price']
    category_input=request.data['category']
    desc_input=request.data['desc']
    image_input=request.data['image']
 
   
    obj=card(
        productId=idProduct_input,
        email=email_input,
        title=title_input,
        price=price_input,
        category=category_input,
        desc=desc_input,
        image=image_input
    )
    obj.save()
    return Response({'message':'Added To Card Successfully'})

@api_view(["POST"])
def get_card(request):
    email_input=request.data['email']
    obj=card.objects.filter(email=email_input).all().values()
    # obj=card.objects.filter(email=email_input).values('productId','email',
    #                             'title','price','category','desc','image')
    
    return Response({"objects":obj})

@api_view(["DELETE"])
def del_card(request):
    id=request.data['productId']
    obj=card.objects.filter(productId=id).delete()
    return Response({"message":"deleted successfullt",
                     'data':obj
                     })



@api_view(['POST'])
def create_address(request,format=None):
    
    email_input=request.data['email']
    name_input=request.data['name']
    phone_input=request.data['phone']

    pin_input=request.data['pin']
    locality_input=request.data['locality']
    add_input=request.data['add']
 
   
    obj=address(
        email=email_input,
        name=name_input,
        phone=phone_input,
        pin=pin_input,
        locality=locality_input,
        add=add_input
    )
    obj.save()
    return Response({'message':'Added Successfully'})

@api_view(["POST"])
def get_address(request):
    email_input=request.data['email']
    obj=address.objects.filter(email=email_input).all().values()
   
    
    return Response({"objects":obj})

# job[0]['company_logo']=companyLogo
    # job[0]['company_name']=companyName
    # job[0]['company_title']=companyTitle
    # job[0]['location']=companyLocation
    # job[0]['date']=companyDate
    # job[0]['job_id']=jobId
    # job[0]['apply_link']=applyLink
    # job[0]['username']=user_name