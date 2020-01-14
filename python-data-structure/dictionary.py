country = {}
country["Bangladesh"] = {"Division":
{

 "Dhaka":{"zilla":13,"Upazilla":93,"council":1833},

 "Barishal":{"zilla":13,"Upazilla":93,"council":1833},

 "Chittagong":{"zilla":13,"Upazilla":93,"council":1833},

 "Khulna":{"zilla":13,"Upazilla":93,"council":1833},

 "Mymensing":{"zilla":13,"Upazilla":93,"council":1833},

 "Rajshahi":{"zilla":13,"Upazilla":93,"council":1833},

 "Rangpur":{"zilla":13,"Upazilla":93,"council":1833},

 "Sylhet":{"zilla":13,"Upazilla":93,"council":1833}

}
}


country["India"] = {"Division":
{

 "kolkata":{"zilla":13,"Upazilla":93,"council":1833},

 "Barishal":{"zilla":13,"Upazilla":93,"council":1833},

 "Chittagong":{"zilla":13,"Upazilla":93,"council":1833},

 "Khulna":{"zilla":13,"Upazilla":93,"council":1833},

 "Mymensing":{"zilla":13,"Upazilla":93,"council":1833},

 "Rajshahi":{"zilla":13,"Upazilla":93,"council":1833},

 "Rangpur":{"zilla":13,"Upazilla":93,"council":1833},

 "Sylhet":{"zilla":13,"Upazilla":93,"council":1833}

}
}


#print("Details of Dhaka:", country["Bangladesh"]["Division"])
for con in country:
    #print(con)
    for div in country["Bangladesh"]["Division"]:
        print(con, div)



for key,value in country.items():

    print("{}:".format(key))
    #print(value)
    for div,value in value.items():
        #print(div)
        #print(value)
        for key,value in value.items():
            print(" ",key,div, "=" ,value)


