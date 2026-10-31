# Lab 01 – Trả lời câu hỏi thảo luận

## 0. Cấu hình `--global` được lưu ở đâu? Khác gì `--local`?

- `--global` lưu ở `~/.gitconfig` (Windows: `C:\Users\<tên>\.gitconfig`), áp dụng cho **mọi repo** của người dùng đó trên máy.
- `--local` lưu ở `.git/config` của **một repo**, chỉ có hiệu lực trong repo đó và **ghi đè** giá trị `--global`.
- Thứ tự ưu tiên: `--local` > `--global` > `--system`. Xem nguồn gốc từng giá trị bằng `git config --list --show-origin`.

## 1. Vì sao dùng `git mv` thay vì xóa rồi tạo tệp mới?

- `git mv dvd.py aims/dvd.py` vừa đổi tên trên đĩa vừa stage thay đổi trong một bước, Git ghi nhận đây là **đổi tên** (rename) chứ không phải "xóa một tệp + thêm một tệp lạ".
- Nhờ vậy lịch sử của tệp không bị đứt: `git log --follow -- aims/cart.py` vẫn thấy các commit từ khi tệp còn ở thư mục gốc, `git blame` vẫn chỉ đúng người viết từng dòng.
- Trên Pull Request, tab *Files changed* hiện "renamed" nên reviewer dễ thấy commit đó không đổi nội dung, chỉ đổi vị trí. (Git thực chất phát hiện đổi tên theo độ giống nội dung, vì thế commit đổi tên nên tách riêng khỏi commit sửa nội dung – đúng như ta đã làm: commit 1 chuyển tệp, commit 2 sửa import.)

## 2. `release/lab01` có phải là baseline không?

Có. Baseline là một phiên bản cấu hình đã được thống nhất, được định danh rõ và chỉ thay đổi qua quy trình kiểm soát. `release/lab01`:

- được tạo từ `master` sau khi PR #1 đã review và merge (đã qua kiểm soát thay đổi);
- trỏ đúng vào một commit xác định (`git rev-parse origin/master origin/release/lab01` cho cùng mã băm tại thời điểm nộp);
- là "bản giao" cho giảng viên chấm, sau này chỉ được sửa qua `hotfix/*` + PR.

Tuy nhiên nhánh vẫn có thể di chuyển (khi hotfix), nên để định danh **bất biến** cho baseline ta còn gắn **annotated tag** (`v0.1.0`) ở Lab 04.

## 3. Vì sao không commit thẳng lên `master` dù làm một mình?

- **Kỷ luật quy trình:** `master` là dòng tích hợp luôn chạy được; mọi thay đổi đi qua nhánh + PR thì `master` không bao giờ ở trạng thái dở dang.
- **Truy vết:** PR ghi lại mục đích, mô tả, cách kiểm thử và liên kết Issue – đó là "change request" trong SCM. Commit thẳng thì mất hết thông tin này.
- **Dễ hoàn tác:** một tính năng = một PR = một merge commit, cần gỡ thì `git revert -m 1` một lần.
- **Chuẩn bị cho làm nhóm và CI:** branch protection, review, kiểm thử tự động (GitHub Actions) đều gắn với PR; tập thói quen ngay từ khi làm một mình.
- Lịch sử nhánh/PR cũng là bằng chứng quá trình làm việc dùng để đối chiếu với kế hoạch sprint của BTL.
