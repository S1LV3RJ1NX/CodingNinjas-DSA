def isValidIPv4(ipAddress):
    
    if "." in ipAddress:
        lst = ipAddress.split(".")

        if len(lst)==4 and all( len(octate) > 0 and 
                                ((len(octate)==1 and "0" <= octate <= "9") or # if single digit then must be between 0 and 9
                                (octate.isdigit() and octate[0] != "0" and 1<= int(octate) <= 255)) # else between 1 and 255
                                for octate in lst):
            return True
    return False


tc = int(input())

for _ in range(tc):
    ip = input().strip()

    ans = isValidIPv4(ip)
    print(ans)