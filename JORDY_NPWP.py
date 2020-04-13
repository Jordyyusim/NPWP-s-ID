
def cekNPWP(id):
    a = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9','-', '.']
    syarat = True
    if len(id) != 20:
        syarat = False
    if id[0] != '0':
        syarat = False
    if id[2] != '.' and id[6] != '.' and id[10] != '.' and id[16] != '.':
        syarat = False
    if id[12] != '-':
        syarat = False
    for i in id:
        if i not in a:
            syarat = False
    if syarat:
        Identitas_Wajib_Pajak = id[0:2] 
        Nomor_Registrasi = id[3:10] 
        Alat_Pengaman = id[11]
        Kode_KPP = id[13:16] 
        Status_Wajib_Pajak = id[17:21]
        if Identitas_Wajib_Pajak == '01' or Identitas_Wajib_Pajak == '02' or Identitas_Wajib_Pajak == '03':
            identitas = 'Wajib Pajak Badan'
        elif Identitas_Wajib_Pajak == '04' or Identitas_Wajib_Pajak == '06':
            identitas = 'Wajib Pajak Pengusaha'
        elif Identitas_Wajib_Pajak == '05':
            identitas = 'Wajib Pajak Karyawan'
        elif Identitas_Wajib_Pajak == '07' or Identitas_Wajib_Pajak == '08' or Identitas_Wajib_Pajak == '09':
            identitas = 'Wajib Pajak Orang Pribadi'
        print('Kode Seri NPWP Valid')
        print('Identitas Wajib Pajak:', Identitas_Wajib_Pajak ,identitas)
        print('Nomor Registrasi:', Nomor_Registrasi)
        print('Alat Pengaman:', Alat_Pengaman)
        print('Kode KPP:', Kode_KPP)
        print('Status Wajib Pajak', Status_Wajib_Pajak)
    else:
        print('Kode Seri NPWP Tidak Valid')

cekNPWP("02.123.456.0-212.191")
