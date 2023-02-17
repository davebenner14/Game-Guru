from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import ProgressForm
from .models import Vid, Character
from django.urls import reverse_lazy



from .models import Vid

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def vids_index(request):
  vids = Vid.objects.all()
  return render(request, 'vids/index.html', { 'vids': vids })

def vids_detail(request, vid_id):
  vid = Vid.objects.get(id=vid_id)
  id_list = vid.characters.all().values_list('id')
  characters_vid_doesnt_have = Character.objects.exclude(id__in=id_list)
  progress_form = ProgressForm()
  return render(request, 'vids/detail.html', { 'vid': vid, 'progress_form': progress_form, 'characters': characters_vid_doesnt_have 
  })

class VidCreate(CreateView):
  model = Vid
  fields = ['name', 'console', 'genre', 'release']

class VidUpdate(UpdateView):
  model = Vid
  fields = ['console', 'genre', 'release']

class VidDelete(DeleteView):
  model = Vid
  success_url = '/vids'

def add_progress(request, vid_id):
    form = ProgressForm(request.POST)
    if form.is_valid():
      new_progress = form.save(commit=False)
      new_progress.vid_id = vid_id
      new_progress.save()
    return redirect('detail', vid_id=vid_id)


class CharacterList(ListView):
  model = Character

class CharacterDetail(DetailView):
  model = Character

class CharacterCreate(CreateView):
  model = Character
  fields = ['name', 'color']

  def get_success_url(self):
        return reverse_lazy('characters_list')

class CharacterUpdate(UpdateView):
  model = Character
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Character
  success_url = '/characters'

def assoc_character(request, vid_id, character_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Vid.objects.get(id=vid_id).characters.add(character_id)
  return redirect('detail', vid_id=vid_id)

def unassoc_character(request, vid_id, character_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Vid.objects.get(id=vid_id).characters.add(character_id)
  return redirect('detail', vid_id=vid_id)


