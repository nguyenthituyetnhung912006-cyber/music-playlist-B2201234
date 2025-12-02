import sys

# Khai báo biến danh sách toàn cục
songs = []

def add_song(title, artist, duration):
    """Thêm một bài hát mới vào danh sách songs."""
    try:
        duration_sec = int(duration)
    except ValueError:
        print("Lỗi: Thời lượng phải là số nguyên (giây).")
        return

    new_song = {
        'title': title,
        'artist': artist,
        'duration': duration_sec
    }
    songs.append(new_song)
    print(f"✅ Đã thêm bài hát: '{title}' - {artist}")


def main():
    """Hiển thị menu chọn chức năng cơ bản."""
    while True:
        print("\n--- 🎧 ỨNG DỤNG QUẢN LÝ PLAYLIST 🎧 ---")
        print("1. Thêm bài hát (Feature 1)")
        print("2. Xem danh sách phát (Feature 2)")
        print("3. Tìm bài hát theo ca sĩ (Feature 3)")
        print("4. Thoát")

        choice = input("Nhập lựa chọn của bạn (1-4): ")

        if choice == '1':
            print("\n--- THÊM BÀI HÁT ---")
            title = input("Nhập tên bài hát: ")
            artist = input("Nhập tên ca sĩ: ")
            duration = input("Nhập thời lượng (giây): ")
            add_song(title, artist, duration)
        elif choice == '2':
            print("Chức năng 'Xem danh sách phát' chưa được triển khai.")
        elif choice == '3':
            print("Chức năng 'Tìm bài hát' chưa được triển khai.")
        elif choice == '4':
            print("Tạm biệt! 👋")
            sys.exit(0)
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()