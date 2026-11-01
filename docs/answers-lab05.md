# Lab 05 – Trả lời câu hỏi thảo luận

## 1. Vì sao ở Phần A chưa gắn tag `v1.1.0`?

Tag là định danh **bất biến** của một phiên bản đã phát hành. Ở Phần A, `release/lab05` mới được cắt ra và ta biết sắp phải đưa bản sửa lỗi `search_by_title` vào. Nếu đã gắn `v1.1.0` thì sau khi cherry-pick bản sửa, nội dung nhánh không còn khớp tag; không được di chuyển tag đã chia sẻ, nên buộc phải phát hành `v1.1.1`. Chưa gắn tag → đưa bản sửa vào trước, rồi mới gắn `v1.1.0` lên đúng nội dung cuối cùng.

## 2. Vì sao không merge cả nhánh hotfix vào `master`?

Nhánh hotfix có 2 commit: (1) sửa lỗi + test, (2) `chore: bump version to 1.0.1`. Commit (2) chỉ đúng cho dòng 1.0.x; trên `master` đang là 1.1.0 nên merge sẽ xung đột hoặc hạ phiên bản. Vì vậy commit sửa lỗi được tách riêng và chỉ **cherry-pick -x** commit đó sang `master` và `release/lab05`; `-x` thêm dòng `(cherry picked from commit <FIX_SHA>)` để truy vết nguồn gốc.

## 3. Ưu, nhược điểm của *upstream first* so với *release first*

| | Upstream first (Microsoft Release Flow) | Release first (học phần) |
|---|---|---|
| Cách làm | Sửa trên `master` trước, cherry-pick xuống các `release/*` | Sửa trên `release/*` bị lỗi trước, cherry-pick lên `master` và release khác |
| Ưu điểm | Không bao giờ "quên" sửa master → không tái phát lỗi ở bản sau; master luôn là nguồn sự thật; bản sửa được kiểm thử với mã mới nhất | Bản vá cho người dùng ra **nhanh**, sửa và test đúng trên mã đã phát hành; hợp khi master đã khác xa bản phát hành |
| Nhược điểm | Bản sửa viết trên master có thể không áp được vào release cũ (code đã khác) → cherry-pick xung đột; người dùng bản cũ phải chờ | Dễ quên lan truyền về master/release khác → lỗi quay lại ở bản sau (regression); cần bước kiểm toán (Phần F) |

## 4. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F phát hiện?

- `git tag --contains <FIX_SHA>` và `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`: chỉ thấy 1 bản cherry-pick (master) thay vì 2; `v1.1.0` không nằm trong danh sách.
- `git cherry -v origin/release/lab05 origin/release/lab04`: commit `fix: make search_by_title case-insensitive` hiện dấu `+` (release/lab05 chưa có bản tương đương).
- Vòng lặp kiểm tra hành vi trên `v1.0.1 v1.1.0 master` sẽ in `0` cho `v1.1.0` thay vì `1` – đây là kiểm tra trực tiếp nhất.

## 5. CI với GitHub Actions

`.github/workflows/ci.yml` chạy `python -m unittest discover -s tests -v` cho mọi PR vào `master` và `release/**`. Bật *Require status checks to pass* trong rule của `master`; PR thử `bugfix/ci-demo` cố ý làm hỏng `total_cost` → CI đỏ → nút Merge bị khóa, PR được đóng không merge.
