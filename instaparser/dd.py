import instaloader
import os
import pickle
import time
import requests
import qrcode
import random
import sys
import django
from django.conf import settings
from django.http import HttpRequest
from datetime import datetime

sys.path.append('C:/Users/dg078/Desktop/asdd/zzz')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kestesikz.settings")
django.setup()

def download_posts_data(posts_per_account, pickle_directory, media_directory, base_url):
    max_retries = 20
    retries = 0

    while retries < max_retries:
        try:
            L = instaloader.Instaloader()

            # Замените 'your_instagram_username' и 'your_instagram_password' на ваши реальные учетные данные
            username = 'tw3az'
            password = '888kaz888'

            L.context.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
            L.context.debug = True

            L.login(username, password)

            # Определение текущего дня недели
            current_weekday = datetime.now().weekday()

            # Формирование пути к пикл-файлу текущего дня
            current_instagram_pickle_path = os.path.join(pickle_directory, f"{current_weekday + 2}.pickle")

            with open(current_instagram_pickle_path, 'rb') as instagram_data_file:
                instagram_data = pickle.load(instagram_data_file)

            accounts_data = []
            media_url_prefix = settings.MEDIA_URL

            # Загрузите существующие данные, если файл уже существует
            common_instagram_pickle_path = os.path.join(pickle_directory, 'common_instagram_data.pickle')
            if os.path.exists(common_instagram_pickle_path):
                with open(common_instagram_pickle_path, 'rb') as common_instagram_pickle_file:
                    existing_data = pickle.load(common_instagram_pickle_file)
            else:
                existing_data = []

            for data in instagram_data:
                account_name = data.get('account_name')
                school_id = data.get('school')

                if account_name is None or not account_name:
                    print("Error: 'account_name' key is missing or empty in account data. Skipping.")
                    continue

                print(f"Processing account {account_name} from school {school_id}")

                try:
                    profile = instaloader.Profile.from_username(L.context, account_name)
                except instaloader.exceptions.ProfileNotExistsException:
                    print(f"Profile {account_name} does not exist.")
                    continue

                account_data = []

                count = 0
                for post in profile.get_posts():
                    post_id = str(post.mediaid)
                    if any(existing_post['id'] == post_id for existing_post in existing_data):
                        print(f"Post {post_id} already exists. Skipping.")
                        continue
                    if count >= posts_per_account:
                        break

                    # Проверка наличия идентификатора поста в существующих данных

                    post_data = {
                        'id': post_id,
                        'text': post.caption,
                        'timestamp': post.date_utc.timestamp(),
                        'media': [],
                        'qr_code': None,
                        'login': account_name,
                        'school': school_id
                    }

                    try:
                        if post.is_video:
                            print('video')
                            media_data = {}

                            time.sleep(random.uniform(10, 15))

                            video_url = f"https://www.instagram.com/p/{post.shortcode}/"
                            qr_code_path = os.path.join(media_directory, f"{post.mediaid}_video_qr.png")

                            qr = qrcode.QRCode(
                                version=1,
                                error_correction=qrcode.constants.ERROR_CORRECT_L,
                                box_size=10,
                                border=4,
                            )
                            qr.add_data(video_url)
                            qr.make(fit=True)

                            img = qr.make_image(fill_color="black", back_color="white")
                            img.save(qr_code_path)
                            print(f"Generated QR code for video: {qr_code_path}")

                            post_data['qr_code'] = f"{base_url}{media_url_prefix}{os.path.relpath(qr_code_path, settings.MEDIA_ROOT).replace(os.path.sep, '/')}"

                            post_data['media'].append(media_data)

                        elif post.typename == 'GraphSidecar':
                            print('karusel')
                            for index, node in enumerate(post.get_sidecar_nodes()):
                                media_data = {}

                                time.sleep(random.uniform(3, 6))

                                if node.is_video:
                                    video_url = f"https://www.instagram.com/p/{post.shortcode}/"
                                    qr_code_path = os.path.join(media_directory, f"{post.mediaid}_video_qr.png")

                                    qr = qrcode.QRCode(
                                        version=1,
                                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                                        box_size=10,
                                        border=4,
                                    )
                                    qr.add_data(video_url)
                                    qr.make(fit=True)

                                    img = qr.make_image(fill_color="black", back_color="white")
                                    img.save(qr_code_path)
                                    print(f"Generated QR code for video: {qr_code_path}")

                                    post_data['qr_code'] = f"{base_url}{media_url_prefix}{os.path.relpath(qr_code_path, settings.MEDIA_ROOT).replace(os.path.sep, '/')}"

                                    post_data['media'].append(media_data)
                                else:
                                    time.sleep(random.uniform(3, 6))

                                    media_file_name = f"{post.mediaid}_{index + 1}.jpg"
                                    media_data[f'post_photos_{index + 1}'] = f"{base_url}{media_url_prefix}instaparser/{media_file_name}"

                                    media_file_path = os.path.join(settings.MEDIA_ROOT, 'instaparser', media_file_name)
                                    with open(media_file_path, 'wb') as media_file:
                                        media_file.write(requests.get(node.display_url).content)

                                    post_data['media'].append(media_data)
                                    print(f"Downloaded media for post {post.mediaid}: {media_data}")

                        else:
                            print('foto')
                            media_data = {}
                            time.sleep(random.uniform(3, 6))

                            media_file_name = f"{post.mediaid}_1.jpg"
                            media_data[f'post_photos_1'] = f"{base_url}{media_url_prefix}instaparser/{media_file_name}"

                            media_file_path = os.path.join(settings.MEDIA_ROOT, 'instaparser', media_file_name)
                            with open(media_file_path, 'wb') as media_file:
                                media_file.write(requests.get(post.url).content)

                            post_data['media'].append(media_data)
                            print(f"Downloaded media for post {post.mediaid}: {media_data}")

                        account_data.append(post_data)
                        count += 1
                        time.sleep(random.uniform(3, 6))

                    except Exception as e:
                        print(f"Failed to fetch metadata for post {post.mediaid}. Error: {e}")

                accounts_data.extend(account_data)

            # Добавьте новые данные в существующие
            existing_data.extend(accounts_data)

            # Сохраните обновленные данные обратно в common_instagram_data.pickle
            with open(common_instagram_pickle_path, 'wb') as common_instagram_pickle_file:
                pickle.dump(existing_data, common_instagram_pickle_file)

            print(f"Данные Instagram успешно добавлены в общий pickle файл: {common_instagram_pickle_path}")

            break

        except instaloader.exceptions.InstaloaderException as e:
            print(f"Ошибка при входе в аккаунт Instagram: {e}")
            retries += 1
            if retries < max_retries:
                print(f"Повторная попытка {retries}/{max_retries} через 5 минут...")
                time.sleep(5*60)
            else:
                print("Достигнуто максимальное количество попыток. Программа завершает выполнение.")
                sys.exit(1)
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
            sys.exit(1)

# Остальной код
if __name__ == "__main__":
    posts_per_account = 1
    pickle_directory = 'C:/Users/dg078/Desktop/asdd/zzz/instaparser/'
    base_url = "http://127.0.0.1:8000/"
    media_directory = os.path.join(settings.MEDIA_ROOT, 'instaparser')

    download_posts_data(posts_per_account, pickle_directory, media_directory, base_url)
