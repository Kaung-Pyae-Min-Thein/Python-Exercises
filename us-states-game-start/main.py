import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
# screen obj ထဲမှာ image ကို shape အဖြစ်ထည့်ပြီးတော့မှ turtle shape ကို img အဖြစ်သုံးလို့ရတာ
screen.addshape(image)
turtle.shape(image)
text = turtle.Turtle()
text.hideturtle()
text.penup()

states_not_complete = True

states_dataframe = pandas.read_csv("50_states.csv")
states_list = states_dataframe["state"].to_list()
total_states = len(states_list)
guessed_state = []
while len(guessed_state) <= 50:
        user_ans = screen.textinput(title=f"{len(guessed_state)}/{total_states} States Correct",
                                    prompt="Type the State's name.").title()
        if user_ans == "Exit":
                break
        # if user correct
        elif user_ans in states_list:
                # get the user answer and retrieve positions x,y
                answer_row = states_dataframe[states_dataframe["state"] == user_ans]
                x_pos = int(answer_row.x)
                y_pos = int(answer_row.y)
                text.goto(x=x_pos, y=y_pos)
                text.write(answer_row.state.item())
                # text.write(arg=user_ans, align="center")
                guessed_state.append(user_ans)
# states to learn csv
missing_states = []
for each_state in states_list:
        if each_state not in guessed_state:
                missing_states.append(each_state)
new_frame = pandas.DataFrame(missing_states)
new_frame.to_csv("states_to_learn.csv")

# screen ကို click ရင် Screen ရဲ့ x,y values တွေ return ပြန်တယ်
# def get_mouse_click_coor(x,y):
#         print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# keep screen open
# screen.mainloop()
