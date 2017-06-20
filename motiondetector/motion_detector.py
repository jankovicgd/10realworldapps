import cv2, time, pandas
from datetime import datetime

first_frame = None
status_list = [None, None]
noframes = 0
video = cv2.VideoCapture(0)
times = []
df = pandas.DataFrame(columns=["Start", "End"])

while True:
    noframes += 1
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0) # increases accuracy and reduces noise

    if noframes == 50:
        first_frame = gray

    if first_frame is not None:
        delta_frame = cv2.absdiff(first_frame, gray)
        thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_delta = cv2.dilate(thresh_delta, None, iterations = 2)

        (_, cnts, _) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour) < 10000:
                continue
            status = 1  # motion detected

            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        status_list.append(status)
        if status_list[-1] == 1 and status_list[-2] == 0:
            times.append(datetime.now())
        if status_list[-1] == 0 and status_list[-2] == 1:
            times.append(datetime.now())
        cv2.imshow("Gray Frame", gray)
        cv2.imshow("Delta Frame", delta_frame)
        cv2.imshow("Threshold Frame", thresh_delta)
        cv2.imshow("Color Frame", frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            if status == 1:
                times.append(datetime.now())
            break

for i in range(0, len(times), 2):
    df = df.append({"Start":times[i], "End": times[i + 1]}, ignore_index = True)

df.to_csv("times.csv")

video.release()
cv2.destroyAllWindows()
