class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def safe_note(self):
        with open('notes.txt', 'a') as file:
            file.write(f'{self.title}:{self.content}|')

    @staticmethod
    def read_notes():
        with open('notes.txt', 'r') as file:
            notes = file.read().split('|')[:-1]
        return [Note(title.strip(), content.strip()) for (title, content) in 
                (note.split(':', 1) for note in notes)]
    
    @staticmethod
    def edit_note(title, new_content):
        with open('notes.txt', 'r') as file:
            notes = file.read().split('|')[:-1]
    
        edit_note = []
        for note in notes:
            t_title, t_content = note.split(':', 1)
            if t_title.strip() == title.strip():
                note = f'{t_title}:{new_content}'
            edit_note.append(note.strip())
        
        with open('notes.txt', 'w') as file:
            file.write('|'.join(edit_note) + '|')


    @staticmethod
    def delete_note(title):
        with open('notes.txt', 'r') as file:
            notes = file.read().split('|')[:-1]
        
        residue_notes = []
        for note in notes:
            current_title, _ = note.split(':', 1)
            if current_title.strip() != title.strip():
                residue_notes.append(note.strip())
        
        with open('notes.txt', 'w') as file:
            file.write('|'.join(residue_notes) + '|')
    
    @staticmethod
    def clear_note(notes):
        with open('notes.txt', 'r') as file:
            notes = file.read().split('---')[:-1]
        
        residue_notes = []
        for note in notes:
            t_title, _ = note.split('n', 1)
            if t_title.strip() != title.strip():
                residue_notes.append(note.strip())
        
        with open('notes.txt', 'w') as file:
            file.write('n---n'.join(residue_notes) + 'n---n')



if __name__ == '__main__':
    while True:
        print('Выберите действие: ')
        print('1. Создать заметку')
        print('2. Читать список заметок')
        print('3. Редактировать заметку')
        print('4. Удалить заметку')
        print('5. Выйти')
    
        choice = input('Введите номер действия: ')

        if choice == '1':
            title = input('Введите заголовок заметки: ')
            content = input('Введите содержание заметки: ')
            note = Note(title, content)
            note.safe_note()
            print('Заметка успешно создана.')
        
        elif choice == '2':
            notes = Note.read_notes()
            if notes:
                print('Список заметок: ')
                for i, note in enumerate(notes, 1):
                    print(f'{i}. {note.title}')
            else:
                print('Заметок нет')

        elif choice == '3':
            title = input('Введите заголовок заметки, которую необходимо отредактировать: ')
            new_content = input('Введите новое содержание заметки: ')
            Note.edit_note(title, new_content)
            print('Заметка успешно отредактирована.')
        
        elif choice == '4':
            title = input('Введите заголовок заметки, которую необходимо удалить: ')
            Note.delete_note(title)
            print('Заметка успешно удалена.')

        elif choice == '5':
            break

        else:
            print('Неверный выбор.')