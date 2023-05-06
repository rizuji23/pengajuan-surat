$(document).ready(() => {
    $("#type_surat").change((e) => {
        const type = e.target.value;
        const nik = $("#nik").val()
        var content = "";
        $("#form-pengajuan").attr('action', `/save_${type}`);
        console.log(type);

        switch (type) {
            case "nikah":
                content = `
                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Nama Mempelai Pria</label>
                    <div class="col-md-10">
                        <input required name="mempelai_pria" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Nama Mempelai Wanita</label>
                    <div class="col-md-10">
                        <input required name="mempelai_wanita" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Nama Wali</label>
                    <div class="col-md-10">
                        <input required name="nama_wali" class="form-control" id=""/>
                    </div>
                </div>

                <h4 class="header-title">Persyaratan</h4>
                <hr>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Surat Pengantar RT/RW</label>
                    <div class="col-md-10">
                        <input required name="surat_rt_rw" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Fotocopy Kartu Tanda Penduduk (calon suami/istri)</label>
                    <div class="col-md-10">
                        <input required name="ktp" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Fotocopy Kartu Keluarga (calon suami/istri)</label>
                    <div class="col-md-10">
                        <input required name="kk" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Fotocopy Akta Lahir (calon suami/istri)</label>
                    <div class="col-md-10">
                        <input required name="akta_lahir" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Fotocopy Ijazah Terakhir (calon suami/istri)</label>
                    <div class="col-md-10">
                        <input required name="ijazah" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Pas Foto (calon suami/istri)</label>
                    <div class="col-md-10">
                        <input required name="foto_pas_1" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Surat pernyataan belum pernah menikah, yang di tandatangani oleh Calon Pengantin dan Pengurus RT/RW, formulir ini bisa di dapat dari Kelurahan atau RT/TW setempat</label>
                    <div class="col-md-10">
                        <input required name="surat_belum_nikah" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Surat pernyataan persetujuan orang tua / wali yang di tandatangani oleh Orang Tua, Saksi dan Pengurus RT/RW, formulir(N1-N4) ini juga bisa di dapat dari Kelurahan atau RT/RW setempat</label>
                    <div class="col-md-10">
                        <input required name="surat_persetujuan" type="file" class="form-control" id=""/>
                    </div>
                </div>
                `;
                break;
            
            case 'surat_kelahiran':
                content = `
                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Nama Bayi</label>
                    <div class="col-md-10">
                        <input required name="nama_bayi" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Tanggal Lahir</label>
                    <div class="col-md-10">
                        <input required name="tanggal_lahir" class="form-control" type="date" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Jenis Kelamin Anak</label>
                    <div class="col-md-10">
                        <select class="form-control" name="jenis_kelamin_anak">
                            <option value="">Pilih Jenis Kelamin</option>
                            <option value="Laki-Laki">Laki-Laki</option>
                            <option value="Perempuan">Perempuan</option>
                        </select>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Hari Jam Lahir</label>
                    <div class="col-md-10">
                        <input required name="hari_jam_lahir" class="form-control" type="datetime-local" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Anak Ke</label>
                    <div class="col-md-10">
                        <input required name="anak_ke" class="form-control" type="number" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Nama Ibu</label>
                    <div class="col-md-10">
                        <input required name="nama_ibu" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Nama Ayah</label>
                    <div class="col-md-10">
                        <input required name="nama_ayah" class="form-control" id=""/>
                    </div>
                </div>

                <h4 class="header-title">Persyaratan</h4>
                <hr>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Surat Pengantar RT/RW</label>
                    <div class="col-md-10">
                        <input required name="surat_rt_rw" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Fotocopy Surat dari Bidan/Rumah Sakit</label>
                    <div class="col-md-10">
                        <input required name="surat_dokter" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Fotocopy Kartu Keluarga</label>
                    <div class="col-md-10">
                        <input required name="kk" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Fotocopy KTP Orangtua</label>
                    <div class="col-md-10">
                        <input required name="ktp" type="file" class="form-control" id=""/>
                    </div>
                </div>
                `
                break;
            
            case 'surat_pindah':
                content = `
                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Alamat Asal</label>
                    <div class="col-md-10">
                        <textarea class="form-control" name="alamat_asal"></textarea>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Pindah Ke</label>
                    <div class="col-md-10">
                        <textarea class="form-control" name="pindah_ke"></textarea>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Pengikut</label>
                    <div class="col-md-10">
                        <textarea class="form-control" name="pengikut"></textarea>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Keterangan</label>
                    <div class="col-md-10">
                        <textarea class="form-control" name="keterangan"></textarea>
                    </div>
                </div>

                <h4 class="header-title">Persyaratan</h4>
                <hr>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Surat Pengantar (Formulir Surat Pindah) dari Desa</label>
                    <div class="col-md-10">
                        <input required name="surat_rt_rw" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Kartu Keluarga (KK) Asli</label>
                    <div class="col-md-10">
                        <input required name="kk" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Kartu Tanda Penduduk (KTP) Asli</label>
                    <div class="col-md-10">
                        <input required name="ktp" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Pas Photo</label>
                    <div class="col-md-10">
                        <input required name="pas_foto" type="file" class="form-control" id=""/>
                    </div>
                </div>
                `;
                break;
            
            case 'skck':
                content = `
                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Keperluan</label>
                    <div class="col-md-10">
                        <textarea class="form-control" name="keperluan"></textarea>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Keterangan</label>
                    <div class="col-md-10">
                        <textarea class="form-control" name="keterangan"></textarea>
                    </div>
                </div>

                <h4 class="header-title">Persyaratan</h4>
                <hr>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Fotokopi Kartu Tanda Penduduk (KTP) atau Surat Izin Mengemudi (SIM)</label>
                    <div class="col-md-10">
                        <input required name="sim" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Fotokopi Kartu Keluarga (KK)</label>
                    <div class="col-md-10">
                        <input required name="kk" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">
                    Fotokopi Akta Kelahiran/Surat Kenal Lahir/Ijazah Terakhir</label>
                    <div class="col-md-10">
                        <input required name="akta" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">
                    Pas foto 4x6 berlatar/background merah</label>
                    <div class="col-md-10">
                        <input required name="pas_foto" type="file" class="form-control" id=""/>
                    </div>
                </div>
                `;
                break;
            
            case 'sku':
                content = `
                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Nama Usaha</label>
                    <div class="col-md-10">
                        <input required name="nama_usaha" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Jenis Usaha</label>
                    <div class="col-md-10">
                        <input required name="jenis_usaha" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Alamat Usaha</label>
                    <div class="col-md-10">
                        <textarea class="form-control" name="alamat_usaha"></textarea>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Keterangan</label>
                    <div class="col-md-10">
                        <textarea class="form-control" name="keterangan"></textarea>
                    </div>
                </div>

                <h4 class="header-title">Persyaratan</h4>
                <hr>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Surat Pengantar (Formulir Surat Pindah) dari Desa</label>
                    <div class="col-md-10">
                        <input required name="surat_pengantar" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Kartu Keluarga (KK) Asli</label>
                    <div class="col-md-10">
                        <input required name="kk" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Kartu Tanda Penduduk (KTP) Asli</label>
                    <div class="col-md-10">
                        <input required name="ktp" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Pas Photo</label>
                    <div class="col-md-10">
                        <input required name="pas_foto" type="file" class="form-control" id=""/>
                    </div>
                </div>
                `
                break;
            
            case 'sktm_kes':
                content = `
                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Nama Anggota Keluarga</label>
                    <div class="col-md-10">
                        <input required name="nama_anggota_keluarga" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Hubungan</label>
                    <div class="col-md-10">
                        <input required name="hubungan" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Keterangan</label>
                    <div class="col-md-10">
                        <textarea class="form-control" name="keterangan"></textarea>
                    </div>
                </div>

                <h4 class="header-title">Persyaratan</h4>
                <hr>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Surat Pengantar RT/RW</label>
                    <div class="col-md-10">
                        <input required name="surat_pengantar" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Foto Copy E-ktp elektronik (KTP)</label>
                    <div class="col-md-10">
                        <input required name="ktp" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Foto Copy Kartu Keluarga (KK)</label>
                    <div class="col-md-10">
                        <input required name="kk" type="file" class="form-control" id=""/>
                    </div>
                </div>
                `
                break;

            case 'sktm_pend':
                content = `
                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Nama Tanggungan</label>
                    <div class="col-md-10">
                        <input required name="nama_tanggungan" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Jumlah Tanggungan</label>
                    <div class="col-md-10">
                        <input required name="jml_tanggungan" class="form-control" type="number" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Hubungan Tanggungan</label>
                    <div class="col-md-10">
                        <input required name="hubungan_tanggungan" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Keterangan</label>
                    <div class="col-md-10">
                        <textarea class="form-control" name="keterangan"></textarea>
                    </div>
                </div>

                <h4 class="header-title">Persyaratan</h4>
                <hr>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Surat Pengantar RT/RW</label>
                    <div class="col-md-10">
                        <input required name="surat_pengantar" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Foto Copy E-ktp elektronik (KTP)</label>
                    <div class="col-md-10">
                        <input required name="ktp" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Foto Copy Kartu Keluarga (KK)</label>
                    <div class="col-md-10">
                        <input required name="kk" type="file" class="form-control" id=""/>
                    </div>
                </div>
                `
                break;

            case 'domisili':
                content = `
                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Keterangan</label>
                    <div class="col-md-10">
                        <textarea class="form-control" name="keterangan"></textarea>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Masa Berlaku</label>
                    <div class="col-md-10">
                        <input required name="masa_berlaku" class="form-control" type="date" id=""/>
                    </div>
                </div>

                <h4 class="header-title">Persyaratan</h4>
                <hr>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Kartu Keluarga (KK) asli dan fotokopi</label>
                    <div class="col-md-10">
                        <input required name="kk" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">KTP asli dan fotokopi</label>
                    <div class="col-md-10">
                        <input required name="ktp" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Pas Photo</label>
                    <div class="col-md-10">
                        <input required name="pas_foto" type="file" class="form-control" id=""/>
                    </div>
                </div>
                `;
                break;

            case 'beda_nama':
                content = `
                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Dokumen Keliru</label>
                    <div class="col-md-10">
                        <input type="file" name="dokumen_keliru"/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Dokumen Benar</label>
                    <div class="col-md-10">
                        <input type="file" name="dokumen_benar"/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Keterangan</label>
                    <div class="col-md-10">
                        <textarea class="form-control" name="keterangan"></textarea>
                    </div>
                </div>
                
                <h4 class="header-title">Persyaratan</h4>
                <hr>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Pengantar RT RW</label>
                    <div class="col-md-10">
                        <input required name="surat_pengantar" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Fotocopy KTP</label>
                    <div class="col-md-10">
                        <input required name="ktp" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Fotocopy KK</label>
                    <div class="col-md-10">
                        <input required name="kk" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Fotocopy Dokumen yang Terdapat Perbedaan Data</label>
                    <div class="col-md-10">
                        <input required name="dokumen_pembeda" type="file" class="form-control" id=""/>
                    </div>
                </div>
                `;
                break;

            case 'surat_kematian':
                content = `
                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Nama Wafat</label>
                    <div class="col-md-10">
                        <input required name="nama_wafat" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Penyebab</label>
                    <div class="col-md-10">
                        <input required name="penyebab" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Hari Tanggal Wafat</label>
                    <div class="col-md-10">
                        <input required name="hari_tanggal_wafat" class="form-control" type="date" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Pelapor</label>
                    <div class="col-md-10">
                        <input required name="pelapor" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Hubungan Pelapor</label>
                    <div class="col-md-10">
                        <input required name="hubungan_pelapor" class="form-control" id=""/>
                    </div>
                </div>

                <h4 class="header-title">Persyaratan</h4>
                <hr>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">KTP dan KK asli almarhum</label>
                    <div class="col-md-10">
                        <input required name="ktp_kk" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">KTP asli pasangan almarhum (jika ada pasangan yang masih hidup)</label>
                    <div class="col-md-10">
                        <input required name="ktp_pasangan" type="file" class="form-control" id=""/>
                    </div>
                </div>

                <div class="form-group">
                    <label for="example-text-input" class="col col-form-label">Fotocopy KTP dan KK pelapor</label>
                    <div class="col-md-10">
                        <input required name="ktp_kk_pelapor" type="file" class="form-control" id=""/>
                    </div>
                </div>
                `
                break;
            
            default:
                content = "<p class='text-danger'>Tipe Surat wajib diisi!!.</p>"
        }

        $("#content-form-surat").html(content)
    });

    $("#filter_report").change((e) => {
        const values = $("#filter_report").val();
        console.log(values)
        var data = "";
        switch (values) {
            case "0":
                data = `
                    <input type="text" hidden value="today"/>
                `
                break;
            case "1":
                data = `
                    <div class="form-group">
                        <label for="">Dari Tanggal</label>
                        <input type="date" class="form-control" name="start_date"/>
                    </div>

                    <div class="form-group">
                        <label for="">Sampai Tanggal</label>
                        <input type="date" class="form-control" name="end_date"/>
                    </div>
                `;
                break;
            case '2':
                data = `
                <div class="form-group">
                    <label for="">Sampai Tanggal</label>
                    <input type="month" class="form-control" name="bulan"/>
                </div>
                `
                break;
        }
        $("#filter_box").html(data)
        
    })

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== "") {
          var cookies = document.cookie.split(";");
          for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === name + "=") {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
          }
        }
        return cookieValue;
      }

    var csrftoken = getCookie("csrftoken");

    function csrfSafeMethod(method) {
        return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
      }


    $("#acc_surat").click(() => {
        const data = $("#acc_surat").attr("data");
        const role = $("#acc_surat").attr("role");
        Swal.fire({
            title: 'Apakah yakin?',
            text: "Data pengajuan surat akan disetujui.",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Iya'
          }).then((result) => {
            if (result.isConfirmed) {
                console.log(data);
                $.ajaxSetup({
                    beforeSend: function (xhr, settings) {
                      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                      }
                    },
                  });

                $.ajax({
                    url: 'http://localhost:8000/api/acc_surat',
                    method: "POST",
                    data: {
                        id_laporan: data,
                        status: role,
                    },
                    success: (response) => {
                        if (response.status === true){
                            Swal.fire({
                                icon: 'success',
                                title: 'Berhasil',
                                confirmButtonText: 'Oke',
                                allowOutsideClick: false,
                              }).then((result) => {
                                if (result.isConfirmed) {
                                    if (role === 'petugas') {
                                        document.location.href = '/petugas/dashboard'
                                    } else {
                                        document.location.href = '/kepala/dashboard'
                                    }
                                }
                              });
                        }
                    }
                })
            }
          })
    })

    $("#tolak_surat").click(() => {
        const data = $("#tolak_surat").attr("data");
        const role = $("#acc_surat").attr("role");
        Swal.fire({
            title: 'Apakah yakin?',
            text: "Data pengajuan surat akan ditolak.",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Iya'
          }).then((result) => {
            if (result.isConfirmed) {
                console.log(data);
                $.ajaxSetup({
                    beforeSend: function (xhr, settings) {
                      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                      }
                    },
                  });

                $.ajax({
                    url: 'http://localhost:8000/api/tolak_surat',
                    method: "POST",
                    data: {
                        id_laporan: data,
                        status: role,
                    },
                    success: (response) => {
                        if (response.status === true){
                            Swal.fire({
                                icon: 'success',
                                title: 'Berhasil',
                                confirmButtonText: 'Oke',
                                allowOutsideClick: false,
                              }).then((result) => {
                                if (result.isConfirmed) {
                                    if (role === 'petugas') {
                                        document.location.href = '/petugas/dashboard'
                                    } else {
                                        document.location.href = '/kepala/dashboard'
                                    }
                                }
                              });
                        }
                    }
                })
            }
          })
    });

    $('.js-example-basic-single').select2();

    $(".js-example-basic-single").change((e) => {
        const values = e.target.value;
        console.log(values);

        $.ajax({
            url: 'http://localhost:8000/api/get_user',
            method: "GET",
            data: {
                'id': values,
            },
            success: (data) => {
                console.log(data);
                if (data.status === true) {
                    console.log(data.data.nik)
                    $("#nik").val(data.data.nik)
                    $("#nama_pengaju").val(data.data.first_name + ' ' + data.data.last_name)
                }
            }
        })
    });

});