import math
print("Learinig about the ANN and CNN...")
# x1=5    #5 hours study
# x2=6   #6 hours sleep
# w1=0.5 #fixed values for the study (like preference)
# w2=0.2 #fixed values for the sleep  (like preference)
# bias=-1
# z=(x1*w1)+(w2*x2)+bias #this is called nural calculation
# sigmad=1/(1+math.exp(-z))   #Action function calculation using the sigmod function
# print(int(sigmad*100),"% Yor are performance")
def sigmod(z):
  return 1/(1+math.exp(-z))
def sigmod_der(z):
  return (sigmod(z)*(1-sigmod(z)))

# x1=3
# x2=10
# x1=int(input("Enter the hours on website:"))
# x2=int(input("Enter the count of web pages:"))

# x1=3
# x2=10
x1=int(input("Enter the hours on website:"))
x2=int(input("Enter the count of web pages:"))

# w1=0.2
# w2=0.1
with open("shopping_data.txt","r") as f:
  
  l=f.readlines()
  print("length:",len(l),"\n")
  if len(l)>=3:
    
    w1=float(l[0].split("=")[1])
    w2=float(l[1].split("=")[1])
    bias=float(l[2].split("=")[1])
  else:
    w1=0.2
    w2=0.1
    bias=-1

# bias=-1
print(f"w1={w1},w2={w2},b={bias}")
learn_rate=0.1
y_acttual=1
print(f"weight1:{w1},        weight2:{w2},        bias:{bias}")
for i in range(100):
  z=(x1*w1)+(x2*w2)+bias
  y_pre=sigmod(z)
  sq=y_acttual-y_pre
  earror=0.5*(sq*sq)
  earror,y_pre
  # print(f"error{earror},Y_pred{y_pre}")
  derror=-(y_acttual-y_pre)
  dy_dz=sigmod_der(z)
  dw1=x1
  dw2=x2
  db=1
  # print(f"Derror:{derror},dw1={dw1},dw2={dw2},dy_dz={dy_dz}")
  g_w1=derror*dy_dz*dw1
  g_w2=derror*dy_dz*dw2
  g_b=derror*dy_dz*db
  # print(f"g_w1:{g_w1},g_w2:{g_w2},g_b:{g_b}")
  w1-=learn_rate*g_w1
  w2-=learn_rate*g_w2
  bias-=learn_rate*g_b
print(f"weight1:{w1},        weight2:{w2},        bias:{bias},     error:{earror}")
final=int(sigmod(z)*100)
print(f"Final :{final}%")

if(final<=50):
  print("Coustmer can not buy the product")
elif(final>=50 and final<=80):
  print("May buy the product")
else:
  print("Sure Buy the product")      #if want then un comment out to learn this product
#   with open("shopping.txt","w") as f:
#     f.write(f"w1={w1}\n")
#     f.write(f"w2={w2}\n")
#     f.write(f"bias={bias}\n")
#     print("Sucessful of ")