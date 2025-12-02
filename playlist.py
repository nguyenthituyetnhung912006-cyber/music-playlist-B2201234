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
# ... (giữ nguyên hàm add_song)

def view_playlist():
    """Duyệt và in ra thông tin tất cả bài hát trong playlist."""
    if not songs:
        print("Danh sách phát hiện đang trống.")
        return

    print("\n--- 🎶 DANH SÁCH PHÁT HIỆN TẠI 🎶 ---")
    for i, song in enumerate(songs):
        # Định dạng thời lượng từ giây sang phút:giây
        minutes = song['duration'] // 60
        seconds = song['duration'] % 60
        # Định dạng hiển thị: 1. **Tên bài hát** - Ca sĩ: Ca sĩ A - Thời lượng: 03:20
        print(f"{i+1}. **{song['title']}** - Ca sĩ: {song['artist']} - Thời lượng: {minutes:02d}:{seconds:02d}")
    print("------------------------------------------")

# ... (giữ nguyên hàm add_song và view_playlist)

def search_by_artist(artist_name):
    """Tìm và in ra các bài hát của một ca sĩ."""
    # Lọc các bài hát có tên ca sĩ khớp (không phân biệt chữ hoa/thường)
    found_songs = [song for song in songs if song['artist'].lower() == artist_name.lower()]

    if not found_songs:
        print(f"Không tìm thấy bài hát nào của ca sĩ '{artist_name}'.")
        return

    print(f"\n--- 🔎 KẾT QUẢ TÌM KIẾM CỦA CA SĨ '{artist_name}' 🔎 ---")
    for i, song in enumerate(found_songs):
        minutes = song['duration'] // 60
        seconds = song['duration'] % 60
        # Định dạng: 1. **Tên bài hát** - Thời lượng: 03:20
        print(f"{i+1}. **{song['title']}** - Thời lượng: {minutes:02d}:{seconds:02d}")
    print("---------------------------------------------------------")

def main():
    # ... (menu giữ nguyên)

    choice = input("Nhập lựa chọn của bạn (1-4): ")

    if choice == '1':
        # ... (giữ nguyên code add_song)
        pass
    elif choice == '2':
        # ... (giữ nguyên code view_playlist)
        pass
    elif choice == '3':
        print("\n--- TÌM BÀI HÁT THEO CA SĨ ---")
        artist_name = input("Nhập tên ca sĩ cần tìm: ")
        search_by_artist(artist_name) # <--- Gọi hàm mới
    elif choice == '4':
        # ... (giữ nguyên code thoát)
        pass
    else:
        # ... (giữ nguyên báo lỗi)
        pass

if __name__ == "__main__":
    main()




