#!/usr/bin/env python3
import os
import re

def get_required_imports(content):
    imports = set()
    
    # Kiểm tra các type cần thiết
    if 'Column' in content:
        imports.add('Column')
    if 'Integer' in content:
        imports.add('Integer')
    if 'String' in content:
        imports.add('String')
    if 'Boolean' in content:
        imports.add('Boolean')
    if 'DateTime' in content:
        imports.add('DateTime')
    if 'ForeignKey' in content:
        imports.add('ForeignKey')
    if 'Text' in content:
        imports.add('Text')
    if 'Date' in content:
        imports.add('Date')
    if 'UUID' in content:
        imports.add('UUID')
    if 'Table' in content:
        imports.add('Table')
    
    return imports

def update_model_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Lấy các import cần thiết
    required_imports = get_required_imports(content)
    
    # Tạo phần import mới
    imports = []
    if required_imports:
        imports.append(f"from sqlalchemy import {', '.join(sorted(required_imports))}")
    imports.append("from sqlalchemy.orm import relationship")
    imports.append("from sqlalchemy.sql import func")
    imports.append("from app.db.base_class import Base")
    
    # Thêm import UUID nếu cần
    if 'UUID' in required_imports:
        imports.append("from sqlalchemy.dialects.postgresql import UUID")
        imports.append("import uuid")
        imports.append("")
        imports.append("def generate_uuid():")
        imports.append("    return str(uuid.uuid4())")
    
    # Thay thế phần import cũ
    new_content = re.sub(
        r'from app\.models\.base import \*\n',
        '\n'.join(imports) + '\n\n',
        content
    )
    
    # Thay thế datetime.datetime.utcnow bằng func.now()
    new_content = re.sub(
        r'datetime\.datetime\.utcnow',
        'func.now()',
        new_content
    )
    
    # Xóa các import không cần thiết
    new_content = re.sub(
        r'import datetime\n',
        '',
        new_content
    )
    
    with open(file_path, 'w') as f:
        f.write(new_content)

def main():
    models_dir = 'app/models'
    for filename in os.listdir(models_dir):
        if filename.endswith('.py') and filename != '__init__.py' and filename != 'base.py':
            file_path = os.path.join(models_dir, filename)
            print(f'Updating {filename}...')
            update_model_file(file_path)

if __name__ == '__main__':
    main() 