import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import argparse
import os
import glob
from datetime import datetime
from dotenv import dotenv_values
from logger import logger

from app import *

class IFBuilderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JDA Interface file Builder")
        self.root.geometry("600x500")
        
        # Apply a modern theme (choose from: 'cosmo', 'flatly', 'darkly', etc.)
        self.style = ttk.Style(theme='flatly')
        
        # Environment selection with debug option
        self.env_frame = ttk.Labelframe(
            self.root, 
            text="Environment", 
            padding=(10, 5), 
            bootstyle=PRIMARY
        )
        self.env_frame.pack(fill=X, padx=10, pady=5)
        
        # Environment radio buttons
        self.env_var = ttk.StringVar(value="uat")
        self.uat_rb = ttk.Radiobutton(
            self.env_frame, 
            text="UAT", 
            variable=self.env_var, 
            value="uat",
        )
        self.prod_rb = ttk.Radiobutton(
            self.env_frame, 
            text="Production", 
            variable=self.env_var, 
            value="prod",
            bootstyle="danger"
        )
        
        self.uat_rb.pack(side=LEFT, padx=5)
        self.prod_rb.pack(side=LEFT, padx=5)
        # Immediately disable environment selection since debug is checked by default
        self.uat_rb.config(state=DISABLED)
        self.prod_rb.config(state=DISABLED)
        
        # Debug switch (modern toggle)
        self.debug_var = ttk.BooleanVar(value=True)
        self.debug_switch = ttk.Checkbutton(
            self.env_frame, 
            text="Debug Mode",
            variable=self.debug_var,
            bootstyle="round-toggle",
            command=self.toggle_env_selection
        )
        self.debug_switch.pack(side=RIGHT, padx=5)
        
        # Build options - using a combobox
        self.options_frame = ttk.Labelframe(
            self.root, 
            text="Build Type", 
            padding=(10, 5),
            bootstyle=INFO
        )
        self.options_frame.pack(fill=X, padx=10, pady=5)
        
        self.build_options = ["ORDER", "PA", "SKU"]
        self.build_var = ttk.StringVar()
        
        ttk.Label(
            self.options_frame, 
            text="Select build type:",
            bootstyle=INFO
        ).pack(anchor=W, pady=2)
        
        self.build_combo = ttk.Combobox(
            self.options_frame, 
            textvariable=self.build_var,
            values=self.build_options,
            bootstyle=INFO,
            state="readonly"
        )
        self.build_combo.pack(fill=X, padx=5, pady=5)
        self.build_combo.current(0)
        
        # Filename suffix
        self.name_frame = ttk.Labelframe(
            self.root, 
            text="Output Filename Suffix (optional)", 
            padding=(10, 5),
            bootstyle=SECONDARY
        )
        self.name_frame.pack(fill=X, padx=10, pady=5)
        
        self.name_entry = ttk.Entry(
            self.name_frame,
            bootstyle=INFO
        )
        self.name_entry.pack(fill=X, padx=5, pady=5)
        
        # Execute button
        self.execute_button = ttk.Button(
            self.root, 
            text="Execute", 
            command=self.execute_build,
            bootstyle=SUCCESS
        )
        self.execute_button.pack(pady=10)
        
        # Log output
        self.log_frame = ttk.Labelframe(
            self.root, 
            text="Log Output", 
            padding=(10, 5),
            bootstyle=SECONDARY
        )
        self.log_frame.pack(fill=BOTH, expand=YES, padx=10, pady=5)
        
        self.log_text = ttk.Text(
            self.log_frame, 
            height=10, 
            state=DISABLED,
            wrap=WORD,
            font=('Courier New', 10)
        )
        self.log_text.pack(fill=BOTH, expand=YES, padx=5, pady=5)
        
        # Add scrollbar with TTKBootstrap style
        scrollbar = ttk.Scrollbar(
            self.log_text,
            bootstyle=ROUND
        )
        scrollbar.pack(side=RIGHT, fill=Y)
        self.log_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.log_text.yview)
    
    def toggle_env_selection(self):
        """Enable/disable environment radio buttons based on debug mode"""
        debug_mode = self.debug_var.get()
        state = DISABLED if debug_mode else NORMAL
        
        self.uat_rb.config(state=state)
        self.prod_rb.config(state=state)
        
        if debug_mode:
            self.env_var.set("uat")
            self.log_message("Debug mode enabled - environment selection disabled")
        else:
            self.log_message("Debug mode disabled - environment selection enabled")
        
    def log_message(self, message):
        self.log_text.config(state=NORMAL)
        self.log_text.insert(END, message + "\n")
        self.log_text.see(END)
        self.log_text.config(state=DISABLED)
        
    def execute_build(self):
        # Disable UI
        self.execute_button.config(state=DISABLED, text="Processing...")
        self.root.config(cursor="watch")  # Show busy cursor

        # Clear previous logs
        self.log_text.config(state=NORMAL)
        self.log_text.delete(1.0, END)
        self.log_text.config(state=DISABLED)
        
        # Prepare arguments
        args = argparse.Namespace()
        args.debug = self.debug_var.get()
        args.environment = self.env_var.get()
        args.name = self.name_entry.get() or None
        
        # Set build type based on selection
        selected_build = self.build_var.get().lower()
        args.order = selected_build == "order"
        args.pa = selected_build == "pa"
        args.sku = selected_build == "sku"
            
        try:
            self.log_message(f"Build type: {selected_build.upper()}")
            self.log_message(f"Debug mode: {'ON' if args.debug else 'OFF'}")
            
            if not args.debug:
                self.log_message(f"Environment: {args.environment.upper()}")
            
            # Check environment file (skip if in debug mode)
            if not args.debug and not os.path.isfile(f'.env.{args.environment}'):
                error_msg = f'.env.{args.environment} does not exist'
                self.log_message(f"ERROR: {error_msg}")
                ttk.dialogs.Messagebox.show_error(
                    title="Error",
                    message=error_msg,
                    parent=self.root
                )
                return
            
            # Simulate the build process
            name_prefix = args.name or ''
            suffix_with_ymdhms = f'{name_prefix}_{datetime.now().strftime("%y%m%d%H%M%S")}'
            input_file = 'IF_Input.xlsx'
            message = []
            if args.order:
                message.append(build_order_header(input_file, suffix_with_ymdhms))
                message.append(build_order_line(input_file, suffix_with_ymdhms))
            elif args.pa:
                message.append(build_pa_header(input_file,suffix_with_ymdhms))
                message.append(build_pa_line(input_file, suffix_with_ymdhms))
            elif args.sku:
                message.append(build_sku(input_file, suffix_with_ymdhms))

            self.log_message('\n'.join(msg for msg in message if msg))
            
            # Simulate SFTP upload (skip in debug mode)
            if not args.debug:
                env = dotenv_values(f'.env.{args.environment}')
                sftp_upload(host=env.get('sftp_host'), port=env.get('sftp_port'),
                    username=env.get('sftp_username'), password=env.get('sftp_password'),
                    remote_folder=env.get('sftp_remote_folder'), filenames=glob.glob(f'IF*{suffix_with_ymdhms}*.txt'),
                    backup=f'backup_{args.environment}',
                    debug_mode=args.debug)
                self.log_message(f"Files uploaded to {args.environment}")
            else:
                self.log_message("Debug mode - skipping file upload")
            
            ttk.dialogs.Messagebox.show_info(
                title="Success",
                message="Build completed successfully",
                parent=self.root
            )
            
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            self.log_message(f"ERROR: {error_msg}")
            logger.exception(e)
            ttk.dialogs.Messagebox.show_error(
                title="Error",
                message=error_msg,
                parent=self.root
            )
        finally:
            # Re-enable UI
            self.execute_button.config(state=NORMAL, text="Execute")
            self.root.config(cursor="")

if __name__ == "__main__":
    root = ttk.Window(themename='flatly')
    root.iconbitmap(os.path.join("rwsif.ico"))
    app = IFBuilderApp(root)
    root.mainloop()