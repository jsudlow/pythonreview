def pairs(s):
    if len(s) % 2 != 0: return False
    case = 'low'
    for i in s:
        print(i)
        print(case)
        if case == 'low':
          if i.isupper():
            print('upper case detected where a lower case char should be')
            return False
          else:
            case = 'high'
            continue

        if case == 'high':
            if i.isupper():
                case = 'low'
            else:
                print('lower case detcted where we should have upper case')
                return False
    return True
print(pairs('aAbB'))
print(pairs('zfff'))
print(pairs('zFz'))
