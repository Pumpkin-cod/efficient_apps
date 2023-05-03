from django.shortcuts import render
from django.http import JsonResponse
# from http import HTTPStatus

# Create your views here.

def gst_number_check(request):
    if request.method == 'POST':
        try:
            number = request.POST.get('gst_numbers')
            if number:
                """
                This function getgstcheck will give the last digit of the gst number
                Output will be given as the last digit which should be as per the given 14 digit number
                :param number: This is the only argument that needs to be given. It is a mandatory Argument.The argument must beat least 14 digit long
                :type gst_no: This parameter must be a string and must be at least digit long
                :return : The function will return the correct last digit of the given gst number
                :raises: There are two errors that will be raised by the Function 
                        1. Type Error: If the parameter entered is not a string, then this error is raised
                        2. Exception: If the parameter entered is not at least 14 digit long, then Exception is raised
                :see also: To know how the GST Ceck sum is calculated , see the alogorithm behind the last digit
                """
                charlist=[char for char in number.upper()]
                a=1
                cumhash=[]

                if not type(number) is str:
                    raise TypeError("Only strings are allowed")
                elif len(str((number)))<14:
                    print ("Please ensure that the input is at least 14 digit long")    
                    pass
                else:    
                    pass
                for i in charlist[0:14:1]:  
                    if a % 2==0:
                        multiplier=2
                    else:
                        multiplier=1
                    if i.isdigit():
                        intvalue=int(i)
                        prod=intvalue*multiplier
                        quotient=prod//36
                        remain=prod%36
                        hash=quotient+remain    
                    else:
                        intvalue=ord(i)-55   
                        prod=intvalue*multiplier
                        quotient=prod//36
                        remain=prod%36
                        hash=quotient+remain
                    a=a+1
                    cumhash.append(hash)
                hashsum=(sum(cumhash))
                remain=hashsum%36
                checksum=36-remain
                if checksum<10:
                    finalchk=str(checksum)
                elif checksum==36:
                    finalchk=str(0)
                else:
                    finalchk=chr(checksum+55)
                # return (finalchk)
                print(finalchk,"\n\n\n\n")
                return JsonResponse({"success": finalchk}, status=200)
            else:
                return JsonResponse({"error": "GST number missing"},status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500) 
    return render(request, 'gst/check_number.html')