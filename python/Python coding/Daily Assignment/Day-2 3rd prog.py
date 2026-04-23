col={"yellow","red","green","orange","blue"}
for colours in col:
    print(colours)
col.add("sky blue")
col.remove("blue")
print("updated colours:",col)
col1={"pink","litepink","thickpink"}
print("intersection:",col &col1)
print("difference:",col-col1)
print("union:",col|col1)
print("is red in the list:",red in col &col1)
