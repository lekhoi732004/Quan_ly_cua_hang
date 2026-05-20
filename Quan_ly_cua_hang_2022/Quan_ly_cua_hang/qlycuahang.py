#Quản lý hóa đơn
import os, csv
import libs.xu_ly_cua_hang
#from csv import reader
_path="files/ds_cua_hang.csv"
lstcuahang=[]
#--------Hàm thứ nhất-----------------------------------------------------
def mo_file_cua_hang(_path,lstcuahang):
    try:
        f=open(_path,'r', encoding ='utf-8')
        for dong in csv.reader(f):
            if dong[0]=='mã cửa hàng':
                continue
            lstcuahang.append({'mã cửa hàng':dong[0], 'tên cửa hàng':dong[1],'vốn đầu tư':dong[2],'doanh thu':dong[3]})
        f.close()
        return 1
    except Exception as ex1:
        print('Không mở được file hợp lệ !! ', ex1)
    return
#--------Hàm thứ hai---------------------------------------------------
def luu_ds_cua_hang(_path,lstcuahang):
    try:
        f=open(_path,'w',newline='', encoding = 'utf-8')
        csv.writer(f).writerow(['mã cửa hàng','tên cửa hàng','vốn đầu tư','doanh thu'])
        for hd in lstcuahang:
            csv.writer(f).writerow([hd['mã cửa hàng'], hd['tên cửa hàng'],hd['vốn đầu tư'],hd['doanh thu']])
        f.close()
        return 1
    except Exception as ex1:
        return 0
#--------Hàm thứ ba-----------------------------------------------------
def them_cua_hang(lstcuahang):
    while True:
        ma_cuahang=input('Nhập mã cửa hàng: ')
        ten_cuahang=input('Nhập tên cửa hàng: ')
        doanhthu=int(input('Doanh thu của cửa hàng: '))
        vondautu=float(input('Vốn đầu tư: '))
        if vondautu <= 50000000:
            thue=float((5/100)*vondautu)
        else:
            thue=float((10/100)*vondautu)
        thuc_thu=float(doanhthu-thue)
        lstcuahang.append({'mã cửa hàng':ma_cuahang,'tên cửa hàng':ten_cuahang,\
            'doanh thu':doanhthu,'vốn đầu tư':vondautu,\
        'thuế':thue,'tiền thực thu':thuc_thu,})
    #Hết lệnh append
        tt=input('Bạn có muốn tiếp tục thêm ? (1:TT)')
        if tt != '1':
            print('Mission complete!!!')
            break
    return   
#----------------------------------------------------------------------------------
def in_ds_cua_hang(lstcuahang):
    print('{:12}{:12}{:>20}{:>20}'.format('mã cửa hàng','tên cửa hàng','vốn đầu tư','doanh thu'))
    
    for hd in lstcuahang:
        print('{:12}{:12}{:>20}{:>20}'.format(hd['mã cửa hàng'], hd['tên cửa hàng'],hd['vốn đầu tư'],hd['doanh thu']))

    return
#---------------------------------------------------------------------------------
def tra_cuu_cua_hang(lstcuahang,mach):
    for hd in lstcuahang:
        if hd['mã cửa hàng']==mach:
            return hd
    return
#-------Hàm thống kê 
def thong_ke(lstcuahang):
    tong=0
    tong_thue=0
    lstthongke=[]
    for hd in lstthongke:
            tong+=float(hd['doanh thu'])
            tong_thue+=float(hd['thue'])
    tong_conlai=float(tong-tong_thue)
    print('Tổng doanh thu tất cả các cửa hàng: %f'%tong)
    print('Tổng thuế tất cả các cửa hàng: %f'%tong_thue)
    print('Thực thu của tất cả các cửa hàng: %f'%tong_conlai)
    return 
def xoa_cua_hang(lstcuahang,mach):
    for i in range(len(lstcuahang)):
        hd=lstcuahang[i]
        if hd['mã cửa hàng']==mach:
            del(lstcuahang[i])
            return 1
    return 0
#----------------------------------------------------------------------------------
#sắp xếp cửa hàng thoe thứ tự giảm dần doanh thu
def sapxep(lstcuahang):
    sorted_doanh_thu = sorted(lstcuahang, key=lambda x: x['doanh thu'])
    
    return sorted_doanh_thu 
#----------------------------------------------------------------------------------

#------------BẮT ĐẦU CHƯƠNG TRÌNH-------------------------------
print('CHƯƠNG TRÌNH QUẢN LÝ CỬA HÀNG')
print('#####--- Chương trình được viết bởi nhóm 1 ---#####')
while True:
    print('1: Thêm cửa hàng')
    print('2: Danh sách cửa hàng')
    print('3: Tra cứu cửa hàng')
    print('4: Xóa cửa hàng')
    print('5: Thống kê')
    print('6: Sắp xếp')
    print('7: Lưu danh sách cửa hàng ra file CSV')
    print('8: Đọc file CSV')
   
    chon=int(input('Chọn chức năng cần thực hiện: '))
    if chon ==1:
        them_cua_hang(lstcuahang)
    elif chon==2:
        in_ds_cua_hang(lstcuahang)
    elif chon==3:
        mach=input('Nhập mã cửa hàng cần tra cứu:')
        hd=tra_cuu_cua_hang(lstcuahang,mach)
        if hd==None:
            print("Không tra cứu được mã cửa hàng ")
        else:
            print(hd)
    elif chon==4:
        mach=input('Nhập mã cửa hàng cần xóa: ')
        kt=input('Bạn có chắc chắn muốn xóa không? (c/C hay k/K?')
        if kt =='c' or kt =='C':
            kq=xoa_cua_hang(lstcuahang)
            if kq==1:
                print('Đã xóa cửa hàng mã: ',mach)
            else:
                print('Không tồn tại mã cửa hàng bạn muốn xóa')
    elif chon==5:
        thong_ke(lstcuahang)   
   
    elif chon==6:
        print("Danh sách trước khi sắp xếp theo tổng tiền là:",in_ds_cua_hang(lstcuahang))   
        sapxep(lstcuahang)
        print("Danh sách sau khi sắp xếp theo tổng tiền là:",in_ds_cua_hang(lstcuahang))     
    elif chon==7:
        if luu_ds_cua_hang(_path, lstcuahang)==1:
            print('Lưu thành công !')
        else:
            print('Không lưu được !!!')
        luu_ds_cua_hang(_path, lstcuahang) 
    elif chon==8:
        if mo_file_cua_hang(_path,lstcuahang):
            print("Đã đọc được file vào lstHoaDon ")
    else:
        break
    
    tt=input('Bạn có muốn tiếp tục (1:tt) ')
    
    if tt!='1':
        print('Kết thuc chương trình !!!')
        break
    else: 
        os.system('cls')
    input('Gõ phím bất kỳ để tiếp tục chương trình !!!')
