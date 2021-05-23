# Graph_theory
Source code thực hành môn lí thuyết đồ thị.
+2.1 Giới thiệu
Mô tả sơ bộ về bộ tool của Nhóm: các thư viện cần import, tên và mô tả chức năng của
các hàm nhóm xây dựng được.
+2.1.1 Các thư viện cần import
- os: Thư viện cho phép tạo đường dẫn, tạo thư mục,...
- sys: Dùng để tạo biến dương vô cùng.
- copy: Thư viện dùng để tạo các deepcopy và shallow.
- numpy: Thư viện làm việc với ma trận.
+2.1.2 Hàm nhóm xây dựng được
multigraph(mg)
- generate_adjMatrix: Hàm tạo ra adjacency từ tập đỉnh và tập cạnh.
- generate_InMatrix: Hàm tạo ra Incidence từ tập đỉnh và tập cạnh.
- write_....: là nhóm các hàm viết các đối tượng và file txt.
- read_....: là nhóm các hàm đọc các đối tượng và file txt.
dimultigraph(dmg)
 - generate_adjMatrix: Hàm tạo ra adjacency từ tập đỉnh và tập cạnh.
 - generate_InMatrix: Hàm tạo ra Incidence từ tập đỉnh và tập cạnh.. - write_....: là nhóm các hàm viết các đối tượng và file txt.
 - read_....: là nhóm các hàm đọc các đối tượng và file txt.
 - deg_in: hàm tính bậc vào của một đỉnh.
 - deg_out: hàm tính bậc ra của một đỉnh.
 - succ: hàm tìm đỉnh kề trước.
 - pred: hàm tìm đỉnh kề sau.
- TRANSITIVECLOSURESUCC: tìm tập các đỉnh liên thông trước được đến từ
đỉnh đầu vào.
 - TRANSITIVECLOSUREPRED: tìm tập các đỉnh liên thông sau được đến từ
đỉnh đầu vào.
 - SCC: Hàm tìm các thành phần liên thông.
Các hàm khác:
 - File DIJKSTRA.py:
   + min_distance: Một hàm tiện ích để tìm đỉnh có giá trị khoảng cách nhỏ nhất, từ tập các đỉnh chưa có trong cây đường đi ngắn nhất.
   + printSolution: Hàm để in ra kết quả của thuật toán dijkstra.
   + dijkstra: Hàm cài đặt thuật toán dijkstra.
 - ROY-WARSHALL.py:
     + ROYWARSHALL: Hàm cài đặt thuật toán ROYWARSHALL.
- SPANNINGTREE.py:
    + SPANNINGTREE: Hàm cài đặt thuật toán SPANNINGTREE.
 - DEPTHFIRSTTRAVERSAL.py:
    + DEPTHFIRSTTRAVERSALL: Hàm cài đặt thuật toán DEPTHFIRSTTRAVERSAL.
2.1.3 Cấu trúc file và giải thích :
 -Graph:(Folder chứa dữ liệu của tất cả các đồ thị)
   -Graph_1_1
   -Graph_1_12
   -Graph_1_13
   -Graph_1_18
   -Graph_1_29
 -Graph_tool.py: (File chính cài đặt 2 đối tượng multigraph và dimultigraph )
 -test_multigraph.py: (Kiểm thử các đối tượng trong file Graph_tool.py)
 -Read_graph.py: (Đọc các đồ từ file )
 -Write_graph.py: (Ghi các đồ từ file )
 -DIJKSTRA.py: (cài đặt và kiểm thử thuật toán DIJKSTRA)
 -ROY-WARSHALL.py: (cài đặt và kiểm thử thuật toán ROY-WARSHALL). -SPANNINGTREE.py: (cài đặt và kiểm thử thuật toán SPANNINGTREE)
 - DEPTHFIRSTTRAVERSALL.py: (cài đặt và kiểm thử thuật toán DEPTHFIRSTTRAVERSALL)
 -TRANSITIVECLOSURESUCC.py: (Kiểm thử thuật toán TRANSITIVECLOSURESUCC)

