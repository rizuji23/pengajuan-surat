from django import template

register = template.Library()


@register.simple_tag
def get_url_download(type_surat, id):
    if type_surat == 'nikah':
        return "/download/surat/nikah/{}".format(id)
    elif type_surat == 'surat_kelahiran':
        return "/download/surat/surat_kelahiran/{}".format(id)
    elif type_surat == 'surat_pindah':
        return "/download/surat/surat_pindah/{}".format(id)
    elif type_surat == 'skck':
        return "/download/surat/skck/{}".format(id)
    elif type_surat == 'sku':
        return "/download/surat/sku/{}".format(id)
    elif type_surat == 'sktm_kes':
        return "/download/surat/sktm_kes/{}".format(id)
    elif type_surat == 'sktm_pend':
        return "/download/surat/sktm_pend/{}".format(id)
    elif type_surat == 'domisili':
        return "/download/surat/domisili/{}".format(id)
    elif type_surat == 'beda_nama':
        return "/download/surat/beda_nama/{}".format(id)
    elif type_surat == 'surat_kematian':
        return "/download/surat/surat_kematian/{}".format(id)