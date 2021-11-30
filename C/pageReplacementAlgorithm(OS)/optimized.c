#include<stdio.h>

int page_hit = 0;

int getIndex(int *pages, int total_pages, int current_page, int *frames, int total_frames, int *temp) {
  // check if element present
  for(int i = 0; i < total_frames; i++) {
    if(frames[i] == pages[current_page]) {
      page_hit++;
      return i;
    }
  }
  
  // calculate future index of pages present in pages
  for(int i = 0; i < total_frames; i++) {
    temp[i] = -1;
    for(int j = current_page; j < total_pages; j++) {
      if(frames[i] == pages[j]){
        temp[i] = j;
        break;
      }
    }  
  }

  // return the max index
  int max_index = 0;
  for(int i = 0; i < total_frames; i++) {
    if(temp[i] == -1) {
      return i;
    }
    if(temp[i] > temp[max_index]) {
      max_index = i;
    }
  }
  return max_index;
}

void display(int *frames, int total_frames) {
  for(int i = 0; i < total_frames; i++) {
    printf("%4d", frames[i]);
  }
  printf("\n");
} 

int main() {
  FILE *fp = fopen("page.txt", "r");
  int total_pages, total_frames;
  if (!fp) {
    printf("Error while opening page.txt");
    return 0;
  }
  fscanf(fp, "%d", &total_pages);
  int pages[total_pages];

  for(int i=0; i < total_pages; i++) {
    fscanf(fp, "%d", &pages[i]);
  }
  // read the frame size from file and create array
  fscanf(fp, "%d", &total_frames);
  int frames[total_frames], temp[total_frames];

  // initialize pages with -1
  for(int i = 0; i < total_frames; i++) {
    frames[i] = -1;
    temp[i]   = -1;
  }

  for(int i = 0; i < total_pages; i++) {
    int index = getIndex(pages, total_pages, i, frames, total_frames, temp);
    frames[index] = pages[i];
    display(frames, total_frames);
  }
  printf("page miss: %d", total_pages-page_hit);
  return 0;
}