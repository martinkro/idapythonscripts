segments = dict()
for seg_ea in Segments():
    data = []
    for ea in range(seg_ea,SegEnd(seg_ea)):
        data.append(chr(Byte(ea)))
    print ("SegName:%s" % SegName(seg_ea))
    segments[SegName(seg_ea)] = ''.join(data)

for seg_name,seg_data in segments.items():
    print seg_name,len(seg_data)