# avitoPIX
## CLI photos batch processing tool for Avito classified Ads (and other similar services):
### - **Resize:**
  * less volume = faster upload
  * less resolution = less details to cross-track you in case of several accounts
  * less details to track you (just against mass surveillance) as Avito and similar services typically collect tons of users' data for commercial targetin, users profiling, moderation and probably to 'call big brother' too
  * changed resolution = different photo, more chances for free repeated Ad posting without blocking
### - **Remove Metadata** (EXIF, file date):
  * less details to track you (see reasons listed above)
### - **Add Phone Number as splitted text label**
  CAUTION! Such labelling's against Avito rules, so your Ad can be blocked during moderation!
  In this case just delete it and create a new one with similar content - for now chances are good!
  * to provide customers with sellers's direct contacts. Starting 2022, for major cities, Avito mandatory uses own proxy phone numbers to isolate customers from sellers. This approach allows them to analyse your phone conversations (!), to collect more data for accounts profiling, commercial targeting, moderating etc

Text label splitted to three parts to hamper ML-driven moderation.
Color for each splitted part selected individually depending on the background color in selected region of the processed photo.
Only jpeg pictures supported. All other formats will be skipped.

Command sintax:

`python avitoPIX.py -in <input_directory> -out <output_directory> -tel <text_label> -y <vertical resolution>`

Command example:

`python avitoPIX.py -in C:\Photo\toProcess -out C:\Photo\processed -tel 8(999)123-45-67`

Directory tree scanned starting from _<input_directory>_ folder. 
All .jpg, .JPG, .jpeg and .JPEG files will be processed as described above.
Processed images stored in similar directory tree starting from _<output_directory>_ as complitely new files (resized, labelled and stripped from metadata) with current data/time stamp. Original photos remain untouched.

## Пакетная обработка фоток для загрузки в объявления Авито (и други подобных сайтов объявлений):
- уменьшаем размер (быстрая загрузка, изменение фото для бесплатной повторной подачи объявления)
- удаляем метаданные (противодествие слежке вообще и для бесплатной повторной подачи в частности)
- добавляем на фото номер телефона (чтобы покупатели звонили не через виртуальный прокси номер с прослушкой, а напрямую)
ВНИМАНИЕ ! Объявления с номером на фото запрещены правилами Авито и могут быть заблокированы. На начало 2022г ручная модерация (с неизбежной блокировкой) встречается не так часто. Автоматическая модерация разбитый на три части телефонный номер пока что пропускает. Если всё же объявление заблокировано - не пытайтесь его исправить - на нём уже стоит "красный флаг", привлекающий внимание модераторов. Удалите заблокированное объявление и, немного подождав, создайте новое с аналогичным содержимым - шаны пока что хорошие.

Цвет для каждой части телефонного номер подбирается автоматически, исходя из цвета фона в данном месте фотки.
Программа сканирует все поддиректории, начиная от указанной, обрабатывает все найденные JPEG файлы (остальные пропускает) и копирует обработанные фотки во вновь созданное  дерево папок, аналогичное по структуре входному. Таким образом, исходные файлы остаются неизменными, а обработанные файлы являются вновь созданными, с атрибутами даты и времени на момент создания. Это дополнительно усложняет слежку со стороны Авито. 
