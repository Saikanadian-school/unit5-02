import ui
#imports ui

def max_array(arraynumbers = []):
    return max(arraynumbers)
#funky gets mac of the array
def findmax(sender):
    list1 = view['textfield1'].text.split(',')
    print ', '.join(list1)
    view['label2'].text = str(max_array(list1))
#prints or views max array

view = ui.load_view()
view.present('sheet')
