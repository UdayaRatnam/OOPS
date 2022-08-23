from Student import student



TITLES = ["Mr.", "Ms.", "Mrs.", "Dr."]

if __name__ ==  "__main__":
    s1 = student("Udaya", "12345", 3.23, "senior")
    s2 = student("Ben", "67891", 3.55, "junior")
    s3 = student("Abby", "23456", 2.26, "freshman")
    s4 = student("Clay", "78912", 1.73, "sophomore")
    s5 = student("Hannah", "34567", 3.83, "freshman")
    s6 = student("Carmen", "89123", 4.00, "sophomore")
    with open('CHS-staff.txt') as f:
        for line in f:
            x = line.split()
            print(x)