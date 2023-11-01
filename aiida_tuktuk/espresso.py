class EspressoDryRunAnalysis:
    """
    This is a class for dealing the dry run message
    """
    def __init__(self, dry_run_node):
        self.options = dry_run_node.get_options()
        self.dry_run_info = dry_run_node.dry_run_info

    def __get_content(self, script_filepath):
        try:
            with open(script_filepath, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File {script_filepath} not found.")
            return f"File {script_filepath} not found."
        except IOError:
            print(f"Error reading {script_filepath}.")
            return f"Error reading {script_filepath}."

    def get_script(self, script_name):
        folder_path = self.dry_run_info['folder']
        script_filepath = f"{folder_path}/{script_name}"
        return self.__get_content(script_filepath)

    def get_input(self):
        script_name = self.options["input_filename"]
        return self.get_script(script_name)

    def get_sbatch(self):
        script_name = self.dry_run_info["script_filename"]
        return self.get_script(script_name)

    def print_input(self):
        print(self.get_input())

    def print_sbatch(self):
        print(self.get_sbatch())

    def print_all(self):
        self.print_sbatch()
        print("--------------------------------------------------------------")
        self.print_input()


def format_latex_labels(labels):
    formatted_labels = []
    for label in labels:
        if "|" in label:  # 如果标签中包含 '|'
            split_labels = label.split("|")
            formatted_split_labels = [format_latex_label(l) for l in split_labels]
            formatted_labels.append("|".join(formatted_split_labels))
        else:
            formatted_labels.append(format_latex_label(label))
    return formatted_labels

def format_latex_label(label):
    if label == "GAMMA":
        return r"$\Gamma$"
    elif "_" in label:
        main, sub = label.split("_")
        return "${}_{{{}}}$".format(main, sub)
    else:
        return "${}$".format(label)
    
def format_path(path):
    path_labels = [path[0][0]]
    for i in range(1, len(path)):
        # 对于每一个段落，检查开始点是否与前一个段落的结束点相同
        if path[i][0] == path[i - 1][1]:
            # 如果相同，则只添加结束点
            path_labels.append(path[i][0])
        else:
            # 如果不同，则添加“开始点|结束点”格式的标签
            path_labels.append(path[i][0] + "|" + path[i-1][1])
    path_labels.append(path[-1][1])
    path_labels_latex = format_latex_labels(path_labels)
    return path_labels_latex

def get_builder_from_baseworkchain(pw_work_chain):
    from aiida.orm import KpointsData
    from aiida_quantumespresso.calculations.pw import PwCalculation
    kpoints = KpointsData()
    kpoints.set_cell_from_structure(pw_work_chain.pw.structure)
    kpoints.set_kpoints_mesh_from_density(pw_work_chain.kpoints_distance.value)
    pw_builder = PwCalculation.get_builder()
    pw_builder.parameters = pw_work_chain.pw.parameters
    pw_builder.kpoints = kpoints
    pw_builder.structure = pw_work_chain.pw.structure
    pw_builder.code = pw_work_chain.pw.code
    pw_builder.metadata = pw_work_chain.pw.metadata
    pw_builder.pseudos = pw_work_chain.pw.pseudos
    return pw_builder
