import face_recognition
import cv2
import numpy as np
import os
import glob


def init_face():
    # Подключение к камере
    video_capture = cv2.VideoCapture(0)

    # списки для загрузки информации ( декодирование , локация лиц etc...)
    known_face_encodings = []
    known_face_names = []
    dirn = os.path.dirname(__file__)
    path = os.path.join(dirn, 'Students/')
    idn = False
    # Список со всеми сохранёнными картинками
    list_of_files = [f for f in glob.glob(path + '*.jpg')]
    # Сколько всего лиц в базе
    number_files = len(list_of_files)

    names = list_of_files.copy()

    for i in range(number_files):
        globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
        globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
        known_face_encodings.append(globals()['image_encoding_{}'.format(i)])
        print(type(known_face_encodings[0]))
        # Список имён , которые мы знаем
        names[i] = names[i].replace('D:\python project\Aface_finder\Students', "")
        buffFoName = names[i]
        buffFoName = buffFoName[1:len(buffFoName) - 4]
        known_face_names.append(buffFoName)
    # Доп переменные
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while idn != True:
        # Захват одного кадра из потока
        ret, frame = video_capture.read()

        # Изменение размера кадра до 1/4 от реального размера для увеличения скорости обработки
        # больше нельзя , меньше то же , иначе лицо не будет попадать в рамку
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Изменение с BGR формата (Которое использует OpenCV) в RGB формат (нужен для face_recognition)
        rgb_small_frame = small_frame[:, :, ::-1]

        # сохраняем декодинг точек лица
        if process_this_frame:
            # Находим все лица на видео и декодируем их
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # Смотрим есть ли совпадения с лицами в базе
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # Чуть быстрее и больше дистанция , но мение точно
                # ''' if True in matches:
                # first_match_index = matches.index(True)
                # name = known_face_names[first_match_index]'''

                # Меньше дистанция , чуть медление но точнее
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    idn = True

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Выводим результаты
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Возвращаем кадр в исходный формат
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # рисуем рамочку
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Выводим подпись под рамкой
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Показываем результат ( видео )
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # После завершения работы скрипта , выключаем камеру и убираем окно
    video_capture.release()
    cv2.destroyAllWindows()
    return idn