from flask import Flask
from operation import AllOperations
from operation_exception import *
app=Flask(__name__)

@app.route('/<operator>/<int:a>/<int:b>')
def performing_operation(operator,a,b):
    obj=AllOperations(a,b)
    try:
        if a>=11 or b>=11:
            raise LimitError('numbers should be less than 11')
        else:
            if operator == '+':
                return obj.add()
            elif operator == '-':
                try:
                    if b>a:
                        raise SubError
                    else:
                        return obj.sub()
                except SubError:
                    a,b=b,a
                    obj_1=AllOperations(a,b)
                    return obj_1.sub()
            elif operator == '*':
                return obj.mul()
            elif operator == 'divided':
                try:
                    if b == 0:
                        raise DivError('no zero in denominator')
                    else:
                        return obj.div()
                except DivError as d:
                    return str(d)
            else:
                return 'your operator is INVALID'
    except LimitError as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
        
   