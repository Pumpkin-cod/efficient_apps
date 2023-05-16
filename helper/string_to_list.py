def string_to_list_converter(gst_numbers):
    gst_list = []
    temp = ""

    for number in range(len(gst_numbers)):
        if gst_numbers[number] != "," and gst_numbers[number] != " ":
            temp += gst_numbers[number]
            if number == len(gst_numbers)-1:
               gst_list.append(temp)
               temp = ""   
        else:
            gst_list.append(temp)
            temp = ""
    return gst_list