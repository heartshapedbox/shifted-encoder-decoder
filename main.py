from tkinter import *
from threading import Timer
import customtkinter
import pyglet
import pyperclip
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\shifted-encoder-decoder')
pyglet.font.add_file('fonts\\Pacifico.ttf')
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')


class App():
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title('Shifted Encoder Decoder')
        self.root.iconbitmap('assets\\encoder.ico')
        x = int(self.root.winfo_screenwidth() // 2.5)
        y = int(self.root.winfo_screenheight() * 0.2)
        x, y = str(x), str(y)
        self.root.geometry(f'525x425+{x}+{y}')
        self.root.resizable(0, 0)
        
        self.accent_color1 = '#212325'
        self.accent_color2 = '#ededed'
        self.accent_color3 = '#3b65ad'
        self.accent_color4 = '#608bd5'
        self.accent_color5 = '#f878b6'
        self.accent_color6 = '#d6478d'
        self.accent_color7 = '#000000'
        self.accent_color8 = '#343638'
        self.accent_color9 = '#ffffff'
        self.accent_header_font1 = ('Pacifico', 22)
        self.accent_header_font2 = ('Pacifico', 10)
        
        self.ch_list = ['a','Z','b','Y','c','X','d','W','e','V','f','U','g','T','h','S','i','R','j','Q','k','P','l','O','m','N','n','M','o','L','p','K','q','J','r','I','s','H','t','G','u','F','v','E','w','D','x','C','y','B','z','A',',','.','?','!',':',';','-','―','_','"','(',')',' ']
        self.encoded_str, self.decoded_str = '', ''
        
        self.show_menu()
        self.root.mainloop()
    
    
    def hover(self, btn, colorfgOnHover, colorfgOnLeave):
        btn.bind("<Enter>", func = lambda i: btn.configure(text_color = colorfgOnHover))
        btn.bind("<Leave>", func = lambda i: btn.configure(text_color = colorfgOnLeave))
    
    
    def show_menu(self):
        self.menu_frame = customtkinter.CTkFrame(self.root, bg_color = (self.accent_color2, self.accent_color1), fg_color = (self.accent_color2, self.accent_color1))
        self.menu_frame.pack(pady = 50)
        
        self.theme_icon_dark = customtkinter.CTkLabel(self.root, text = '🌙', text_font = self.accent_header_font2, text_color = self.accent_color4)
        self.theme_icon_dark.place(x = 32, y = 320, width = 20, height = 20)
        self.theme_icon_light = customtkinter.CTkLabel(self.root, text = '🔆', text_font = self.accent_header_font2, text_color = self.accent_color4)
        
        self.switch_var = customtkinter.StringVar(value = "off")
        self.theme_switch = customtkinter.CTkSwitch(self.root, text = '', command = self.switch_theme, variable = self.switch_var, onvalue = "on", offvalue = "off")
        self.theme_switch.place(x = 25, y = 350)
        self.theme_switch.configure(
            progress_color = self.accent_color4,
            fg_color = self.accent_color4,
            button_color = self.accent_color3,
            button_hover_color = self.accent_color3
        )
        
        self.header_lbl = customtkinter.CTkLabel(self.menu_frame, text = 'Shifted\nEncoder Decoder', text_font = self.accent_header_font1)
        self.header_lbl.pack(pady = 10)
        self.menu_encode_btn = customtkinter.CTkButton(self.menu_frame, cursor = 'hand2', text = 'Encode', command = self.show_encoder_widget)
        self.menu_decode_btn = customtkinter.CTkButton(self.menu_frame, cursor = 'hand2', text = 'Decode', command = self.show_decoder_widget)
        for i in (self.menu_encode_btn, self.menu_decode_btn):
            i.configure(
                bg_color = (self.accent_color2, self.accent_color1),
                fg_color = self.accent_color3,
                text_color = self.accent_color2,
                hover_color = self.accent_color4,
                corner_radius = 6,
                height = 35
                )
            i.pack(pady = 2)
            self.hover(i, self.accent_color3, self.accent_color2)
        
        self.menu_quit_btn = customtkinter.CTkButton(self.menu_frame, cursor = 'hand2', text = 'Quit', command = self.quit)
        self.menu_quit_btn.pack(pady = 2)
        self.menu_quit_btn.configure(
            bg_color = (self.accent_color2, self.accent_color1),
            fg_color = self.accent_color6,
            hover_color = (self.accent_color5, self.accent_color5),
            text_color = self.accent_color2,
            corner_radius = 6,
            height = 35
            )
        self.hover(self.menu_quit_btn, self.accent_color6, self.accent_color2)
    
    
    def switch_theme(self):
        if self.switch_var.get() == 'off':
            self.theme_icon_light.place(x = 1000, y = 1000)
            self.theme_icon_dark.place(x = 32, y = 320, width = 20, height = 20)
            customtkinter.set_appearance_mode('dark')
            self.menu_frame.configure(bg_color = self.accent_color1, fg_color = self.accent_color1)
        else:
            self.theme_icon_dark.place(x = 1000, y = 1000)
            self.theme_icon_light.place(x = 33, y = 320, width = 20, height = 20)
            customtkinter.set_appearance_mode('light')
            self.menu_frame.configure(bg_color = self.accent_color2, fg_color = self.accent_color2)
            self.switch_var.set(value = "on")
    
    
    def close_widget(self):
        self.close_widget_btn.destroy()
        if self.widget_name == 'encoder_widget' and self.switch_var.get() == 'on':
            self.encoder_widget_frame.destroy()
            self.show_menu()
            self.switch_var.set(value = 'on')
        elif self.widget_name == 'encoder_widget' and self.switch_var.get() == 'off':
            self.encoder_widget_frame.destroy()
            self.show_menu()
            self.switch_var.set(value = 'off')
        elif self.widget_name == 'decoder_widget' and self.switch_var.get() == 'on':
            self.decoder_widget_frame.destroy()
            self.show_menu()
            self.switch_var.set(value = 'on')
        else:
            self.decoder_widget_frame.destroy()
            self.show_menu()
            self.switch_var.set(value = 'off')
    
    
    def remove_message(self):
        if self.widget_name == 'encoder_widget':
            self.encoder_copy_message_lbl.configure(text = '')
            self.encoder_reset_message_lbl.configure(text = '')
        else:
            self.decoder_copy_message_lbl.configure(text = '')
            self.decoder_reset_message_lbl.configure(text = '')
        
        
            
    def reset(self):
        if self.widget_name == 'encoder_widget':
            self.encoder_entry.delete(0, END)
            self.encoder_entry.after(500, lambda: self.encoder_entry.focus())
            self.encoder_shift_entry.delete(0, END)
            self.encoder_message.configure(text = '')
            self.encoder_reset_message_lbl.configure(text = 'Reset!')
            Timer(0.5, self.remove_message).start()
        else:
            self.decoder_entry.delete(0, END)
            self.decoder_entry.after(500, lambda: self.decoder_entry.focus())
            self.decoder_shift_entry.delete(0, END)
            self.decoder_message.configure(text = '')
            self.decoder_reset_message_lbl.configure(text = 'Reset!')
            Timer(0.5, self.remove_message).start()
       
    
    def copy(self):
        if self.widget_name == 'encoder_widget':
            pyperclip.copy(self.encoded_str)
            self.encoder_copy_message_lbl.configure(text = 'Copied!')
            Timer(0.5, self.remove_message).start()
        else:
            pyperclip.copy(self.decoded_str)
            self.decoder_copy_message_lbl.configure(text = 'Copied!')
            Timer(0.5, self.remove_message).start()
            
    
    def show_close_widget_button(self):
        self.close_widget_btn = customtkinter.CTkButton(self.root, cursor = 'hand2', text = 'x', command = self.close_widget)
        self.close_widget_btn.place(x = 20, y = 20)
        self.close_widget_btn.configure(
            bg_color = (self.accent_color2, self.accent_color1),
            fg_color = (self.accent_color6, self.accent_color6),
            text_color = self.accent_color2,
            hover_color = (self.accent_color5, self.accent_color5),
            corner_radius = 6,
            width = 25,
            height = 25
        )
        self.hover(self.close_widget_btn, (self.accent_color6, self.accent_color6), self.accent_color2)
    

    def show_encoder_widget(self):
        for i in (self.menu_frame, self.theme_switch, self.theme_icon_dark, self.theme_icon_light):
            i.destroy()
        
        self.widget_name = 'encoder_widget'
        self.encoder_widget_frame = customtkinter.CTkFrame(self.root, bg_color = (self.accent_color2, self.accent_color1), fg_color = (self.accent_color2, self.accent_color1))
        self.encoder_widget_frame.pack(pady = 10)
        self.encoder_header_lbl = customtkinter.CTkLabel(self.encoder_widget_frame, text = 'Encoder', text_font = self.accent_header_font1, anchor = 's', text_color = (self.accent_color6, self.accent_color6))
        self.encoder_header_lbl.grid(row = 0, columnspan = 3, pady = 0)
        self.encoder_input_lbl = customtkinter.CTkLabel(self.encoder_widget_frame, text = 'Input', anchor = 'w', text_color = (self.accent_color7, self.accent_color2))
        self.encoder_input_lbl.grid(row = 1, column = 0, pady = 5, padx = 5, sticky = 'w')
        self.encoder_output_lbl = customtkinter.CTkLabel(self.encoder_widget_frame, text = 'Output', anchor = 'w', text_color = (self.accent_color7, self.accent_color2))
        self.encoder_output_lbl.grid(row = 3, column = 0, padx = 5, sticky = 'w')
        self.encoder_entry = customtkinter.CTkEntry(self.encoder_widget_frame, border_width = 0)
        self.encoder_entry.grid(row = 2, columnspan = 3, pady = 5, padx = 5)
        self.encoder_entry.after(500, lambda: self.encoder_entry.focus())
        self.encoder_entry.configure(width = 400, height = 40)
        self.encoder_message = customtkinter.CTkLabel(self.encoder_widget_frame, corner_radius = 6, text = '', text_color = (self.accent_color7, self.accent_color2), anchor = 'w', wraplength = 390)
        self.encoder_message.grid(row = 4, columnspan = 3, pady = 5, padx = 5)
        self.encoder_message.configure(
            bg_color = (self.accent_color2, self.accent_color1),
            fg_color = (self.accent_color9, self.accent_color8),
            width = 400,
            height = 80
        )
        
        self.encoder_shift_lbl = customtkinter.CTkLabel(self.encoder_widget_frame, text = 'Shift', anchor = 'w', text_color = (self.accent_color7, self.accent_color2))
        self.encoder_shift_lbl.grid(row = 5, column = 0, pady = 15, padx = 5, sticky = 'w')
        self.encoder_shift_entry = customtkinter.CTkEntry(self.encoder_widget_frame, border_width = 0, width = 40)
        self.encoder_shift_entry.grid(row = 5, column = 0, pady = 15, padx = 55, sticky = 'e')
        self.encoder_copy_message_lbl = customtkinter.CTkLabel(self.encoder_widget_frame, text = '', text_color = (self.accent_color3, self.accent_color3), width = 20)
        self.encoder_copy_message_lbl.grid(row = 5, columnspan = 3, pady = 15, padx = 157, sticky = 'e')
        self.encoder_reset_message_lbl = customtkinter.CTkLabel(self.encoder_widget_frame, text = '', text_color = (self.accent_color6, self.accent_color6), width = 20)
        self.encoder_reset_message_lbl.grid(row = 5, columnspan = 3, pady = 15, padx = 37, sticky = 'e')
        self.encoder_encode_btn = customtkinter.CTkButton(self.encoder_widget_frame, cursor = 'hand2', text = 'Encode', command = self.encode)
        self.encoder_encode_btn.grid(row = 6, column = 0, pady = 5, sticky = 'w')
        self.encoder_copy_btn = customtkinter.CTkButton(self.encoder_widget_frame, cursor = 'hand2', text = 'Copy', command = self.copy)
        self.encoder_copy_btn.grid(row = 6, column = 1, pady = 5, sticky = 'e')
        for i in (self.encoder_encode_btn, self.encoder_copy_btn):
            i.configure(
                bg_color = (self.accent_color2, self.accent_color1),
                fg_color = self.accent_color3,
                text_color = self.accent_color2,
                hover_color = self.accent_color4,
                corner_radius = 6,
                width = 110,
                height = 35
                )
            self.hover(i, self.accent_color3, self.accent_color2)
        self.encoder_reset_btn = customtkinter.CTkButton(self.encoder_widget_frame, cursor = 'hand2', text = 'Reset', command = self.reset)
        self.encoder_reset_btn.grid(row = 6, column = 2, pady = 5, sticky = 'e')
        self.encoder_reset_btn.configure(
                bg_color = (self.accent_color2, self.accent_color1),
                fg_color = self.accent_color6,
                hover_color = (self.accent_color5, self.accent_color5),
                text_color = self.accent_color2,
                corner_radius = 6,
                width = 110,
                height = 35
                )
        self.hover(self.encoder_reset_btn, self.accent_color6, self.accent_color2)
        self.show_close_widget_button()
        
        
    def show_decoder_widget(self):
        for i in (self.menu_frame, self.theme_switch, self.theme_icon_dark, self.theme_icon_light):
            i.destroy()
            
        self.widget_name = 'decoder_widget'
        self.decoder_widget_frame = customtkinter.CTkFrame(self.root, bg_color = (self.accent_color2, self.accent_color1), fg_color = (self.accent_color2, self.accent_color1))
        self.decoder_widget_frame.pack(pady = 10)
        self.decoder_header_lbl = customtkinter.CTkLabel(self.decoder_widget_frame, text = 'Decoder', text_font = self.accent_header_font1, anchor = 's', text_color = (self.accent_color6, self.accent_color6))
        self.decoder_header_lbl.grid(row = 0, columnspan = 3, pady = 0)
        self.decoder_input_lbl = customtkinter.CTkLabel(self.decoder_widget_frame, text = 'Input', anchor = 'w', text_color = (self.accent_color7, self.accent_color2))
        self.decoder_input_lbl.grid(row = 1, column = 0, pady = 5, padx = 5, sticky = 'w')
        self.decoder_output_lbl = customtkinter.CTkLabel(self.decoder_widget_frame, text = 'Output', anchor = 'w', text_color = (self.accent_color7, self.accent_color2))
        self.decoder_output_lbl.grid(row = 3, column = 0, padx = 5, sticky = 'w')
        self.decoder_entry = customtkinter.CTkEntry(self.decoder_widget_frame, border_width = 0)
        self.decoder_entry.grid(row = 2, columnspan = 3, pady = 5, padx = 5)
        self.decoder_entry.configure(width = 400, height = 40)
        self.decoder_entry.after(500, lambda: self.decoder_entry.focus())
        self.decoder_message = customtkinter.CTkLabel(self.decoder_widget_frame, corner_radius = 6, text = '', text_color = (self.accent_color7, self.accent_color2), anchor = 'w', wraplength = 390)
        self.decoder_message.grid(row = 4, columnspan = 3, pady = 5, padx = 5)
        self.decoder_message.configure(
            bg_color = (self.accent_color2, self.accent_color1),
            fg_color = (self.accent_color9, self.accent_color8),
            width = 400,
            height = 80
        )

        self.decoder_shift_lbl = customtkinter.CTkLabel(self.decoder_widget_frame, text = 'Shift', anchor = 'w', text_color = (self.accent_color7, self.accent_color2))
        self.decoder_shift_lbl.grid(row = 5, column = 0, pady = 15, padx = 5, sticky = 'w')
        self.decoder_shift_entry = customtkinter.CTkEntry(self.decoder_widget_frame, border_width = 0, width = 40)
        self.decoder_shift_entry.grid(row = 5, column = 0, pady = 15, padx = 55, sticky = 'e')
        self.decoder_copy_message_lbl = customtkinter.CTkLabel(self.decoder_widget_frame, text = '', text_color = (self.accent_color3, self.accent_color3), width = 20)
        self.decoder_copy_message_lbl.grid(row = 5, columnspan = 3, pady = 15, padx = 157, sticky = 'e')
        self.decoder_reset_message_lbl = customtkinter.CTkLabel(self.decoder_widget_frame, text = '', text_color = (self.accent_color6, self.accent_color6), width = 20)
        self.decoder_reset_message_lbl.grid(row = 5, columnspan = 3, pady = 15, padx = 37, sticky = 'e')
        self.decoder_decode_btn = customtkinter.CTkButton(self.decoder_widget_frame, cursor = 'hand2', text = 'Decode', command = self.decode)
        self.decoder_decode_btn.grid(row = 6, column = 0, pady = 5, sticky = 'w')
        self.decoder_copy_btn = customtkinter.CTkButton(self.decoder_widget_frame, cursor = 'hand2', text = 'Copy', command = self.copy)
        self.decoder_copy_btn.grid(row = 6, column = 1, pady = 5, sticky = 'e')
        for i in (self.decoder_decode_btn, self.decoder_copy_btn):
            i.configure(
                bg_color = (self.accent_color2, self.accent_color1),
                fg_color = self.accent_color3,
                text_color = self.accent_color2,
                hover_color = self.accent_color4,
                corner_radius = 6,
                width = 110,
                height = 35
                )
            self.hover(i, self.accent_color3, self.accent_color2)
        self.decoder_reset_btn = customtkinter.CTkButton(self.decoder_widget_frame, cursor = 'hand2', text = 'Reset', command = self.reset)
        self.decoder_reset_btn.grid(row = 6, column = 2, pady = 5, sticky = 'e')
        self.decoder_reset_btn.configure(
                bg_color = (self.accent_color2, self.accent_color1),
                fg_color = self.accent_color6,
                hover_color = (self.accent_color5, self.accent_color5),
                text_color = self.accent_color2,
                corner_radius = 6,
                width = 110,
                height = 35
                )
        self.hover(self.decoder_reset_btn, self.accent_color6, self.accent_color2)
        self.show_close_widget_button()
    
    
    def encode(self):
        self.encoded_str = ''
        self.input_str = self.encoder_entry.get()
        self.shift = int(self.encoder_shift_entry.get())
        self.ch_list_len = len(self.ch_list)
        for i in self.input_str:
            self.finish = False
            while self.finish == False:
                self.ch_index = self.ch_list.index(i)
                if self.ch_index + self.shift >= self.ch_list_len:
                    self.len_diff = self.ch_list_len - self.ch_index
                    self.new_list = [*self.ch_list[self.ch_index:self.ch_list_len],*self.ch_list[0:self.shift - self.len_diff + 1]]
                    if i in self.new_list:
                        self.ch_index = 0
                        self.encoded_str = f'{self.encoded_str}{self.new_list[self.ch_index + self.shift]}'
                else:
                    if i in self.ch_list:
                        self.encoded_str = f'{self.encoded_str}{self.ch_list[self.ch_index + self.shift]}'
                self.encoder_message.configure(text = self.encoded_str)
                self.finish = True
    
    
    def decode(self):
        self.decoded_str = ''
        self.input_str = self.decoder_entry.get()
        self.shift = int(self.decoder_shift_entry.get())
        self.ch_list_len = len(self.ch_list)
        for i in self.input_str:
            self.finish = False
            while self.finish == False:
                self.ch_index = self.ch_list.index(i)
                if self.ch_index - self.shift <= 0:
                    self.len_diff =  self.shift - self.ch_index
                    self.new_list = [*self.ch_list[self.ch_list_len - self.len_diff:self.ch_list_len],*self.ch_list[0:self.ch_index + 1]]
                    if i in self.new_list:
                        self.ch_index = len(self.new_list)
                        self.decoded_str = f'{self.decoded_str}{self.new_list[self.ch_index - self.shift - 1]}'
                else:
                    if i in self.ch_list:
                        self.decoded_str = f'{self.decoded_str}{self.ch_list[self.ch_index - self.shift]}'
                self.decoder_message.configure(text = self.decoded_str)
                self.finish = True
    
    
    def quit(self):
        return quit()


if __name__ == '__main__':
    App()