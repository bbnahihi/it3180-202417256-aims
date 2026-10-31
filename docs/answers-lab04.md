# Lab 04 – Trả lời câu hỏi thảo luận

## 1. Vì sao chuẩn bị phát hành (version, CHANGELOG) trên `master` trước, không sửa trên nhánh release?

- Nhánh `release/*` là **baseline đóng băng**: chỉ nhận hotfix, không nhận phát triển. Nếu sửa version/CHANGELOG trực tiếp trên release thì những thay đổi đó **không có trên `master`** (vì release không bao giờ merge ngược về master) → bản phát hành sau sẽ thiếu mục CHANGELOG, số phiên bản lệch.
- Làm trên `master` qua `topic/prepare-release-1.0.0` + PR thì thay đổi được review như mọi thay đổi khác, và `release/lab04` cắt ra từ `master` sẽ chứa đúng nội dung đó: commit đầu nhánh release = commit trên master = tag `v1.0.0`.

## 2. Vì sao `release/*` không merge (ngược) vào `master`? So sánh với GitFlow

- Trong Release Flow, `master` là dòng phát triển duy nhất, luôn **đi trước** mọi nhánh release. Release được cắt ra từ master, sống song song để bảo trì; mọi thay đổi trên release là hotfix đã/được **cherry-pick** sang master. Merge release vào master sẽ kéo theo cả commit chỉ dành cho dòng cũ (ví dụ `chore: bump version to 1.0.1` ghi đè 1.1.0 trên master) và làm rối lịch sử.
- Kiểm chứng bằng: `git log --oneline master..release/lab04` (kỳ vọng rỗng ngay sau khi cắt release).
- **GitFlow** thì khác: có `develop` (tích hợp) và `main` (bản đã phát hành). Nhánh `release/x.y` tạo từ `develop`, khi xong được merge vào **cả `main` và `develop`**; hotfix tạo từ `main`, merge vào `main` + `develop`. GitFlow hợp với phát hành định kỳ, một phiên bản đang chạy; Release Flow hợp với nhiều phiên bản được bảo trì song song (như các bản nộp lab theo tuần).

## 3. Vì sao lên `1.0.0` mà không phải `0.4.0`?

- Theo SemVer, `0.y.z` là giai đoạn phát triển ban đầu, API chưa ổn định, có thể đổi bất cứ lúc nào. `1.0.0` là lời cam kết **API công khai đã ổn định**; từ đây số MAJOR chỉ tăng khi phá vỡ tương thích.
- Ở Lab 04 ta có đủ chức năng đã review, có test, có CHANGELOG và quy trình phát hành chính thức (nhánh release được bảo vệ, annotated tag, GitHub Release) → đây là bản phát hành "thật" đầu tiên cho người dùng, nên là `1.0.0`. Các bản nộp Lab 01–03 được gắn tag hồi tố `v0.1.0`, `v0.2.0`, `v0.3.0`.

## 4. Tag và nhánh release khác nhau thế nào?

| | Tag `v1.0.0` | Nhánh `release/lab04` |
|---|---|---|
| Di chuyển? | Không bao giờ | Có (khi hotfix) |
| Vai trò | Định danh chính xác một phiên bản | Dòng bảo trì của bản phát hành |

Annotated tag (`git tag -a`) lưu người gắn, ngày và thông điệp – phù hợp đánh dấu baseline. Tag không tự đi theo `git push`, phải `git push origin <tag>`. Tag đã chia sẻ thì không xóa, không di chuyển.
