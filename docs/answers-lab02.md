# Lab 02 – Trả lời câu hỏi thảo luận

## 1. Vì sao phải đồng bộ nhánh với `master` trước khi gửi PR?

- Nhánh `feature/search-by-title` được tạo từ `master` **cũ** (chưa có `print_cart`). Trong lúc đó `master` đã nhận PR khác. Nếu không đồng bộ, thứ được review là mã chạy trên một `master` không còn tồn tại.
- `git merge origin/master` vào nhánh của mình giúp: phát hiện và **tự giải quyết xung đột ngay trên nhánh riêng** (không để reviewer/`master` gánh), và **chạy thử bản tích hợp** (`python main.py`) trước khi merge.
- Đúng nguyên tắc SCM "thứ được duyệt = thứ được tích hợp": khi nhánh đã chứa `master` mới nhất, nội dung reviewer thấy chính là nội dung sẽ vào `master`.
- Nhánh sống ngắn + đồng bộ thường xuyên giúp tránh "merge hell".

## 2. Khi nào **không được** rebase?

- Không rebase các commit **đã chia sẻ** mà người khác đang dựa vào: `master`, `release/*`, hoặc nhánh feature mà đồng đội đã pull về/làm tiếp. Rebase tạo commit mới (SHA mới), viết lại lịch sử; người khác sẽ gặp lịch sử lệch, commit trùng lặp, phải force push.
- Không rebase nhánh có merge commit cần giữ nguyên ý nghĩa (rebase làm phẳng lịch sử).
- Chỉ rebase nhánh **riêng của mình, chưa ai dùng**; nếu đã push thì phải `git push --force-with-lease` và chắc chắn không ai làm trên đó.
- Quy tắc 5 của Release Flow: *viết lại lịch sử (amend, reset, rebase) chỉ trên commit chưa chia sẻ.*

## 3. `feature/*` khác `topic/*` ra sao?

| | `feature/*` | `topic/*` |
|---|---|---|
| Nội dung | Tính năng mới của sản phẩm, thay đổi hành vi chương trình (`print_cart`, `search_by_title`) | Chủ đề không phải tính năng: tài liệu, cấu hình, quy trình (PR template, use case diagram, chuẩn bị phát hành, CI) |
| Ghi CHANGELOG | Thường có (mục *Added*) | Thường không |
| Commit type | `feat:` | `docs:`, `chore:`, `ci:` |

Cả hai đều tạo từ `master`, merge về `master` qua PR.

## 4. So sánh 3 kiểu merge (quan sát từ `git log --oneline --graph`)

| | Merge commit (PR cart-print) | Squash (PR search-by-title) | Rebase (PR use-case) |
|---|---|---|---|
| Giữ commit chi tiết | Có | Không (gộp 1) | Có (SHA mới) |
| Lịch sử tuyến tính | Không | Có | Có |
| Revert cả tính năng | 1 lệnh (`-m 1`) | 1 lệnh | nhiều commit |

Sau squash/rebase, `git branch -d` báo "not fully merged" vì commit trên `master` có SHA khác commit trên nhánh; xác nhận PR đã merged rồi dùng `git branch -D`.
