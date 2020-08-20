from django.shortcuts import render
import razorpay
client=razorpay.Client(auth("rzp_test_AwKU725nvKV3Oo","QqTw9HnfbAkx4XfIHRUUBt3w"))
order_amount = 50000
order_currency = 'INR'
order_receipt = 'order_rcptid_11'

#For Creating Room Information

response=client.order.create(dict(amount=order_amount, currency=order_currency, receipt=order_receipt, payment_capture='0'))

order_id=response["id"]
order_status=response["status"]

if  order_status=="created":
	context["price"]=order_amount
	context["name"]=name
	context["phone"]=phone
	context["email"]=email
	context["order_id"]=order_id
	return render(request,"success.html",context) 

def payment_status(request):

    response = request.POST

    params_dict = {
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_signature' : response['razorpay_signature']
    }


    # VERIFYING SIGNATURE
    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'order_summary.html', {'status': 'Payment Successful'})
    except:
        return render(request, 'order_summary.html', {'status': 'Payment Faliure!!!'})





