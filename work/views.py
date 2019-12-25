from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import vaga_script





def workIndex(request):
    return render(request, 'work/index.html')


def workFindjobs(request):

    #if request.method == 'POST':

    def remove_repetidos(lista):
        l = []
        for i in lista:
            if i not in l:
                l.append(i)
        l.sort()
        return l

    if request.method == 'POST':

        imput_vaga = ''
        imput_vaga = request.POST['job']

        if imput_vaga != '':
            result = vaga_script.read_search(imput_vaga)

            cont = len(result)

            print('\n\n')
            for a in range(len(result)):
                print(result[a][0])
                print(result[a][1])
                print(result[a][2])
                print(result[a][3])

            print('\n\n')

            #return redirect('work-find-jobs', {'result': result})
            return render(request, 'work/findjobs.html', {'result': result,'cont': cont})
        

            #return render(request, 'work/searched.html', {'result': result})
        
        else:
            return redirect('work-find-jobs')

    return render(request, 'work/findjobs.html')



    #return render(request, 'work/findjobs.html')


#def workJob(request, id):
def workJob(request):
    imput_vaga = ''
    imput_vaga = request.POST['job']

    print('\n\n')
    print(imput_vaga)
    print('\n\n')



    return render(request, 'work/job.html')  

def workSearched(request):
    return render(request, 'work/searched.html') 

def workFindjobs2(request):
    return render(request, 'work/findjobs2.html') 


#return render(request, 'conta/fatura.html', {'faturar_x': faturar_x})
'''
def hello(request):
    imput_vaga = 'Desenvolvedor'
    df = vaga_script.read_search(imput_vaga)
    #qs = Product.objects.all()
    #df = read_frame(qs)
    print('\n\n')
    print(df)
    print('\n\n')
    
    dataframe = df.to_html()
    return HttpResponse(dataframe)'''


'''def hello(request):
    return HttpResponse("""
    
    <h1>HELLO</h1>
    
    """)'''
