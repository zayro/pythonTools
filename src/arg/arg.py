def message(**params):
    print(params)
    print(type(params))
    print(params.get('success'))
    print("\n")
    for key, value in params.items():
        print("%s == %s" % (key, value))


dataParams = {"success": True, "data": [], "info": {}}

message(**dataParams)
