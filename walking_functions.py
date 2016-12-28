ea = ScreenEA()
for function_ea in Functions(SegStart(ea),SegEnd(ea)):
    print hex(function_ea),GetFunctionName(function_ea)