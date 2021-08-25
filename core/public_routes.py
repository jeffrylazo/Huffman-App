from core.huffman import Huff_Com, Huff_Dec
from flask import render_template, request, Blueprint 

huffman_translator = Blueprint('huffman_translator',__name__)

@huffman_translator.route('/')
def index():
    return render_template('index.html')


@huffman_translator.route('/compress', methods=['GET','POST'])
def compress():
    data=(None,None,None,True)
    if request.method == 'POST':
        task = Huff_Com(request.form['msg_to_compress'])
        data = (task.get_original_message(),task.get_compressed_message(),task.get_huffman_code(),task.fails)
    return render_template('compress.html', data=data)


@huffman_translator.route('/decompress', methods=['GET','POST'])
def decompress():
    data=(None,None,None,True)
    if request.method == 'POST':
        task = Huff_Dec(request.form['msg_to_decompress'],request.form['msg_key_decompress'])
        data = (task.get_compressed_message(),task.get_decompressed_message_HTML(),request.form.get('msg_key_decompress'),task.fails)

    return render_template('decompress.html', data=data)    