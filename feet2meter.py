def main():
    v = feet2meter((input("Сколько футов:")))


    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):

        b = float(3.281)
        v = str(v)
        v = v.replace("ft","")
        v = float(v)
        v = float(v / b)
        return v

main()
