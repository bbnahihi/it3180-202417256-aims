# Lab 03 – Trả lời câu hỏi thảo luận

## 1. Merge base là gì?

- Merge base là **commit tổ tiên chung gần nhất** của hai nhánh, xem bằng `git merge-base HEAD origin/master`.
- Khi merge, Git thực hiện *three-way merge*: so sánh mỗi bên với merge base. Dòng chỉ một bên sửa → lấy bên đó; dòng **cả hai bên cùng sửa khác nhau** so với merge base → **xung đột**.
- Trong bài: merge base của `feature/show-added-title` và `origin/master` là commit có `print("The disc has been added")`. Dev 1 đổi dòng đó thành tiếng Việt, Dev 2 đổi thành có tiêu đề đĩa → Git không thể tự chọn, đánh dấu `<<<<<<< ======= >>>>>>>` để người giải quyết. Ta kết hợp ý của cả hai: `print(f"Đã thêm đĩa '{dvd.title}' vào giỏ hàng")`.
- Merge base cũng là gốc của phép `A...B` (ba chấm) trên GitHub compare và quyết định PR hiển thị những commit nào (sai base → PR hiện nhiều commit lạ).

## 2. Vì sao trên `master`/`release/*` phải dùng `revert` thay vì `reset`?

- `reset` **dời con trỏ nhánh** về trước, tức là xóa commit khỏi lịch sử. Với nhánh đã chia sẻ, mọi bản clone khác vẫn còn commit đó; lần push sau sẽ bị từ chối hoặc phải `--force`, làm mất công việc của người khác và phá vỡ truy vết.
- `master` và `release/*` được bảo vệ (branch protection: không force push, mọi thay đổi qua PR), nên `reset` + force push vốn bị chặn.
- `revert` **tạo commit mới đảo ngược** thay đổi cũ: lịch sử chỉ được nối thêm, không viết lại; ai cũng pull bình thường; vẫn có thể đi qua nhánh + PR + review; và vết tích "đã thêm rồi gỡ, vì sao" được ghi lại – đúng tinh thần kiểm toán cấu hình.
- Với merge commit cần `git revert -m 1 <sha>`: `-m 1` chọn cha thứ nhất (`master` trước khi merge) làm bản "đúng", đảo ngược toàn bộ thay đổi mà nhánh tính năng mang vào.

## 3. Ghi chú các bước đã làm

- Issue lỗi giới hạn giỏ hàng → `bugfix/cart-limit-off-by-one`: commit `test:` (test **FAIL** – chứng minh test bắt đúng lỗi) đứng **trước** commit `fix:` (test PASS); PR có `Fixes #N` nên Issue tự đóng khi merge vào `master`.
- `bugfix/discount-calculation` tạo từ `origin/feature/discount`, PR có base là `feature/discount` (không phải `master`).
- Xung đột giữa `feature/vietnamese-messages` và `feature/show-added-title` được giải quyết bằng merge `origin/master` vào nhánh, chạy test trước khi commit.
- `topic/undo-practice` (không push) thử `reset --soft/--mixed/--hard` và tìm lại commit bằng `git reflog`; trên lịch sử chung dùng `bugfix/revert-show-added-title` + `git revert -m 1` + PR.
