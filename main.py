import pyautogui as pt
from time import sleep
import pyperclip

sleep(5)

position1 = pt.locateOnScreen("whatsapp/smile.png", confidence=0.6)
x = position1[0]
y = position1[1]


def get_message():
    global x, y

    position = pt.locateOnScreen("whatsapp/smile.png", confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 130, y - 50, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()

    print("Message received: " + whatsapp_message)

    return whatsapp_message


def post_response(message):
    global x, y

    position = pt.locateOnScreen("whatsapp/smile.png", confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)


def process_response(message): # change the option accroding to the need
    if ("hi" or "hello" or "hey") == str(message).lower():
        return "Choose from the given queries: \n A : Capital of India \n B : Capital of TN"
    elif "a" == str(message).lower():
        return "Delhi"
    elif "b" == str(message).lower():
        return "Chennai"
    elif "c" == str(message).lower():
        return "Someone will get back to you shortly"
    else:
        return "Choose from the above given queries, or if you have any other query type C"


def check_for_new_msg():
    pt.moveTo(x + 115, y - 43, duration=.5)
    while True:
        try:
            position = pt.locateOnScreen("whatsapp/green.png", confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)

        except Exception:
            print("no new messagesqdqdq")

        if pt.pixelMatchesColor(int(x + 115), int(y - 50), (255, 255, 255), tolerance=10):
            print("is black ")
            processed_message = process_response(get_message())
            post_response(processed_message)

        else:
            print("no new messages yet")

        sleep(5)


check_for_new_msg()
# processed_message = process_response(get_message())
# post_response(processed_message)
