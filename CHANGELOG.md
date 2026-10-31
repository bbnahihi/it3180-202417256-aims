# Changelog

Mọi thay đổi đáng chú ý của AIMS-mini được ghi tại đây.
Định dạng theo [Keep a Changelog](https://keepachangelog.com/vi/1.1.0/),
phiên bản theo [Semantic Versioning](https://semver.org/lang/vi/).

## [Unreleased]

## [1.0.0] - 2026-11-01
### Added
- `Cart.print_cart()` in danh sách đĩa và tổng tiền, báo "The cart is empty" khi giỏ trống.
- `search_by_title()` tìm DVD theo tiêu đề (`aims/search.py`).
- `Cart.total_cost_with_discount()` tính tổng tiền sau giảm giá, kiểm tra phần trăm hợp lệ.
- Thông báo tiếng Việt khi thêm/xóa đĩa.
- Pull request template, biểu đồ use case (`docs/use-case.md`), bộ test `unittest`.
- In số phiên bản khi chạy `main.py`.

### Changed
- Mã nguồn chuyển vào package `aims/`.

### Fixed
- Giỏ hàng nhận đĩa thứ 21 dù giới hạn là 20 (#8).

