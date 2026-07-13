define chick = ("Hương Nhã")
define main = ("Tôi")
define nerd = ("Tiến Đạt")
define wibu = ("Thịnh Sosuke")
define smoker = ("Duy Trung")

image opening = Transform(
    "00 Scene goc PC.png",
    fit="contain"
)
image pc_hover = "CRT.png"
screen pc_click():

    imagebutton:

        idle "CRT.png"
        hover "CRT.png"
        focus_mask True
        xpos 0
        ypos 0

        action Jump("pc_scene")
label start:
    scene opening
    with fade

    "..."
    "Cuối cùng cũng xong môn rồi, mình phải nhanh chóng tìm trọ thôi. Không thể ở ké nhà dì mãi được."
    "Chắc lên web tìm trọ xem thử, biết đâu tìm được căn nào rẻ rẻ."
    call screen pc_click
