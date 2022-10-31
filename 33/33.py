from fractions import Fraction

results = []

for numerator in range(10, 100):
    for denominator in range(numerator+1, 100):
        string_num = str(numerator)
        string_denom = str(denominator)

        for i in range(1, 10):
            if str(i) in string_num and str(i) in string_denom:
                fake_numerator = string_num.replace(str(i), '', 1)
                fake_denominator = string_denom.replace(str(i), '', 1)

                if int(fake_denominator) == 0:
                    break

                a = Fraction(numerator, denominator)
                b = Fraction(int(fake_numerator), int(fake_denominator))

                if a==b:
                    results.append((numerator, denominator))

one = Fraction(1, 1)

for fraction in results:
    one *= Fraction(fraction[0], fraction[1])

print(one)
